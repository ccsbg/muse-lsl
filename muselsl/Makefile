.PHONY: requirements connect record plot clean

PYTHON ?= python3

requirements:
	pip install -r requirements.txt

muselsl_modified:
	cd .. && pip install -e .

connect:
	muselsl stream --ppg --acc --gyro

record:
	mkdir -p recordings_csv
	@timestamp=$$(date +%Y%m%d_%H%M%S); \
	(muselsl record --duration 60 --type EEG --filename recordings_csv/EEG_$$timestamp.csv & \
	 muselsl record --duration 60 --type PPG --filename recordings_csv/PPG_$$timestamp.csv & \
	 muselsl record --duration 60 --type ACC --filename recordings_csv/ACC_$$timestamp.csv & \
	 muselsl record --duration 60 --type GYRO --filename recordings_csv/GYRO_$$timestamp.csv && wait)

csv_to_json: 
	$(PYTHON) csv_to_json.py

plot:
	muselsl view --version 2

kill:
	-pkill -f "muselsl record" || true
	-pkill -f "muselsl stream" || true

clean:
	rm -rf recordings_csv
	rm -rf recordings_json
