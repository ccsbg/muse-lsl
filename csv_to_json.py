import os
import pandas as pd
from pathlib import Path

def convert_csv_to_json(input_dir="recordings_csv", output_dir="recordings_json"):
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.exists():
        print(f"Input directory '{input_dir}' does not exist.")
        return

    output_path.mkdir(exist_ok=True)

    for csv_file in input_path.glob("*.csv"):
        try:
            df = pd.read_csv(csv_file)
            json_filename = output_path / (csv_file.stem + ".json")
            df.to_json(json_filename, orient="records", lines=True)
            print(f"Converted '{csv_file.name}' to '{json_filename.name}'")
        except Exception as e:
            print(f"Failed to convert '{csv_file.name}': {e}")

if __name__ == "__main__":
    convert_csv_to_json()
