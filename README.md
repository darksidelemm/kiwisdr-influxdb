# kiwisdr-influxdb
KiwiSDR Status to InfluxDB

# KiwiSDR Stats to InfluxDB Collector
Very quickly developed KiwiSDR Status to InfluxDB data collector.

## Setup
```
python3 -m venv venv
pip install -r requirements.txt
```

Edit kiwi_stats.sh and update env vars with appropriate settings.

Setup crontab to run kiwi_stats.sh every minute.

## InfluxDB Stuff
Writes the following fields into the user-defined bucket with the user-defined measurement name:
* todo
