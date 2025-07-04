import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_all_recordings(folder_path='recordings_csv', start_time=None, end_time=None, output_folder='recording_graphs'):
    sns.set_theme(style='whitegrid')
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            if 'timestamps' in df.columns:
                df['timestamps'] = pd.to_numeric(df['timestamps'], errors='coerce')
                if start_time is not None:
                    df = df[df['timestamps'] >= start_time]
                if end_time is not None:
                    df = df[df['timestamps'] <= end_time]
                x = df['timestamps']
                y_columns = [col for col in df.columns if col != 'timestamps']
                xlabel = 'Time (timestamps)'
            else:
                x = df.index
                y_columns = df.columns
                xlabel = 'Index'

            if df.empty:
                print(f"Skipping {filename}: no data in selected timestamp range.")
                continue

            base_name = os.path.splitext(filename)[0]
            for col in y_columns:
                plt.figure(figsize=(12, 6))
                plt.plot(x, df[col])
                plt.title(f'{col} from {filename}')
                plt.xlabel(xlabel)
                plt.ylabel('Signal')
                plt.tight_layout()

                save_path = os.path.join(output_folder, f"{base_name}_{col}.png")
                plt.savefig(save_path)
                plt.close()
                print(f"Saved plot to {save_path}")

def plot_selected_file(folder_path='recordings_csv', output_folder='recording_graphs'):
    sns.set_theme(style='whitegrid')
    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    if not files:
        print("No CSV files found.")
        return

    while True:
        print("\nAvailable files:")
        for i, file in enumerate(files):
            print(f"{i + 1}: {file}")
        print("0: Exit")

        try:
            file_idx = int(input("Enter the number of the file to plot (or 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if file_idx == 0:
            print("Exiting.")
            break

        if not (1 <= file_idx <= len(files)):
            print("Invalid file number. Try again.")
            continue

        selected_file = files[file_idx - 1]
        file_path = os.path.join(folder_path, selected_file)

        df = pd.read_csv(file_path)

        if selected_file.startswith("EEG"):
            expected_columns = ['timestamps', 'TP9', 'AF7', 'AF8', 'TP10', 'Right AUX']
        else:
            expected_columns = ['timestamps', 'X', 'Y', 'Z']

        if not set(expected_columns).issubset(df.columns):
            print("Warning: Expected columns not found in file. Found:", list(df.columns))

        print("\nAvailable columns for plotting (excluding 'timestamps'):")
        available_columns = [col for col in df.columns if col != 'timestamps']
        for i, col in enumerate(available_columns):
            print(f"{i + 1}: {col}")

        selected_indices = input("Enter the column numbers to plot (comma-separated, e.g. 1,3): ")
        try:
            selected_columns = [available_columns[int(i.strip()) - 1] for i in selected_indices.split(',')]
        except (ValueError, IndexError):
            print("Invalid column selection.")
            continue

        filter_by_time = input("Do you want to filter by start and end timestamp? (y/n): ").lower() == 'y'
        if filter_by_time:
            try:
                start_time = float(input("Enter start timestamp: "))
                end_time = float(input("Enter end timestamp: "))
                df['timestamps'] = pd.to_numeric(df['timestamps'], errors='coerce')
                df = df[(df['timestamps'] >= start_time) & (df['timestamps'] <= end_time)]
            except ValueError:
                print("Invalid timestamp values.")
                continue

        if df.empty:
            print("No data in selected timestamp range.")
            continue

        base_name = os.path.splitext(selected_file)[0]

        for col in selected_columns:
            plt.figure(figsize=(12, 6))
            plt.plot(df['timestamps'], df[col])
            plt.title(f"{col} from {selected_file}")
            plt.xlabel("Time (timestamps)")
            plt.ylabel("Signal")
            plt.tight_layout()

            if filter_by_time:
                from_str = str(start_time).replace('.', '_')
                to_str = str(end_time).replace('.', '_')
                save_path = os.path.join(
                    output_folder, 
                    f"{base_name}_{col}_from_{from_str}_to_{to_str}.png"
                )
            else:
                save_path = os.path.join(output_folder, f"{base_name}_{col}.png")

            plt.savefig(save_path)
            print(f"Saved plot to {save_path}")

#plot_all_recordings('recordings_csv')
#plot_selected_file(folder_path='recordings_csv')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Plot EEG/PPG/ACC/GYRO recordings.')
    parser.add_argument('--mode', choices=['all', 'selected'], required=True, help='Choose which plot function to run')
    parser.add_argument('--folder', default='recordings_csv', help='Folder path containing recordings')
    parser.add_argument('--output', default='recordings_graphs', help='Folder to save plots (optional)')
    parser.add_argument('--start', type=float, default=None, help='Start time in seconds (optional)')
    parser.add_argument('--end', type=float, default=None, help='End time in seconds (optional)')

    args = parser.parse_args()

    if args.mode == 'all':
        plot_all_recordings(
            folder_path=args.folder,
            start_time=args.start,
            end_time=args.end,
            output_folder=args.output
        )
    elif args.mode == 'selected':
        plot_selected_file(
            folder_path=args.folder,
            output_folder=args.output
        )

