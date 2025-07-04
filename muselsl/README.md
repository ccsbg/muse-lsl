The following commands should be ran inside the directory "/muselsl".

In order to run this project, you need to have the technologies mentioned "requirments.txt" installed. You can do so by running:

```make requirements```

As this project is a fork of the muse-lsl project, the modified project needs to be installed. You can do so by running:

```make muselsl_modified```

How to run: 

```make connect``` - To connect to the Muse S and stream the EEG, PPG, ACC and GYRO.

```make record``` - To record the EEG, PPG, ACC and GYRO values to a csv value under the folder "/recordings_csv".

```make csv_to_json``` - To convert the files under the folder "/recordings_csv" from csv to json. This will be recorder in folder "/recordings_json".

```make plot_real_time``` - To visualize the EEG's TP9, AF7, AF8, TP10 and Right AUX plots in real-time.

```make plot_all``` - To plot graphs for all csv files under the folder "/recordings_csv". 
Optional parameters:
    START=<timestamp> - Start time (e.g., START=1751533932.557)
   END=<timestamp> - End time (e.g., END=1751533932.901)
   FOLDER=<path> - Folder containing CSV files (e.g., FOLDER=recordings_csv)
   OUTPUT=<path> - Folder to save the plots (e.g., OUTPUT=recording_graphs)
Example: ```make plot_all START=10 END=50 OUTPUT=recordings_graphs FOLDER=recordings_csv```

```make plot_selected``` - To plot selected graphs and respectice selected x and y values.

```make kill``` - To disconnect from Muse S and stop recording. 

```make clean``` - To erase all csv files in folder "/recordings_csv",  "/recordings_json",  "/recordings_graphs".


