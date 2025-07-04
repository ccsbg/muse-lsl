In order to run this project, you need to have the technologies mentioned "requirments.txt" installed. You can do so by running:

```make requirements```

As this project is a fork of the muse-lsl project, the modified project needs to be installed. You can do so by running:

```make muselsl_modified```

How to run: 

```make connect``` - To connect to the Muse S and stream the EEG, PPG, ACC and GYRO.

```make record``` - To record the EEG, PPG, ACC and GYRO values to a csv value under the folder "/recordings".

```make csv_to_json``` - To convert the files under the folder "/recordings" from csv to json.

```make plot``` - To visualize the EEG's TP9, AF7, AF8, TP10 and Right AUX plots.

```make kill``` - To disconnect from Muse S and stop recording. 

```make clean``` - To erase all csv files in folder "/recordings".




