# KiwiSDR Stats to InfluxDB Collector
Very quickly developed KiwiSDR Status to InfluxDB data collector.

## Setup
```
python3 -m venv venv
pip install -r requirements.txt
```

Edit kiwi_stats.sh and update env vars with appropriate settings.

Setup crontab to run kiwi_stats.sh every minute.

## InfluxDB Data Point

Data is added in the following format:
```
{
    'measurement': 'kiwisdr_status', 
    'tags': {'name': 'Members 1'}, 
    'fields': {
        'users': 2, 
        'gps_sats': 5, 
        'snr_full': 31.0, 
        'snr_hf': 31.0, 
        'adc_ov': 37, 
        'uptime': 675950
        }
}
```