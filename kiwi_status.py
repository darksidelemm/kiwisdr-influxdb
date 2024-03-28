#!/usr/bin/env python
#
# Tapo P110 to InfluxDB Collection
#
import requests, sys
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from pprint import pprint

# Collect Environment Variables
KIWISDR_URL = os.environ.get("KIWISDR_URL")
KIWISDR_NAME = os.environ.get("KIWISDR_NAME")
INFLUXDB_URL = os.environ.get("INFLUXDB_URL")
INFLUXDB_TOKEN = os.environ.get("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.environ.get("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.environ.get("INFLUXDB_BUCKET")
INFLUXDB_MEASNAME = os.environ.get("INFLUXDB_MEASNAME")


print(f"KiwiSDR Hostname: \t{KIWISDR_URL}")
print(f"KiwiSDR Name: \t{KIWISDR_NAME}")

print(f"InfluxDB URL: \t{INFLUXDB_URL}")
print(f"InfluxDB Token: \t{INFLUXDB_TOKEN}")
print(f"InfluxDB Org: \t{INFLUXDB_ORG}")
print(f"InfluxDB Bucket: \t{INFLUXDB_BUCKET}")
print(f"InfluxDB Measurement Name: \t{INFLUXDB_MEASNAME}")

# Collect KiwiSDR Status Data

try:
    r = requests.get(KIWISDR_URL)
except Exception as e:
    print(f"Error getting KiwiSDR status: {str(e)}")
    sys.exit(1)

fields = {}

for line in r.text.split("\n"):
    try:
        _fields = line.split("=")
        _name = _fields[0]
        _value = _fields[1]

        #print(f"{_name}: {_value}")

        if _name == "snr":
            fields['snr_full'] = float(_value.split(',')[0])
            fields['snr_hf'] = float(_value.split(',')[1])

        elif _name == "users":
            fields['users'] = int(_value)

        elif _name == "gps_good":
            fields['gps_sats'] = int(_value)

        elif _name == "uptime":
            fields['uptime'] = int(_value)

        elif _name == "adc_ov":
            fields['adc_ov'] = int(_value)

    except Exception as e:
        print(f"Error parsing line ({str(e)}): {line}")


meas_point = {
    "measurement": INFLUXDB_MEASNAME,
    "tags": {"name": KIWISDR_NAME},
    "fields": fields
}

print(meas_point)

# Push into InfluxDB
write_client = influxdb_client.InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

#p = influxdb_client.Point(INFLUXDB_MEASNAME).field("instantaneous_power_w", instantaneous_power_w).field("energy_today_kWh", today_energy_kWh)

write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=meas_point)

print("Done!")