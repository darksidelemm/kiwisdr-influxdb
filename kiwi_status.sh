#!/bin/bash
#
# KiwiSDR Status -> InfluxDB Collection Script
#
# Run with cron on whatever update rate you want
#

# Enter the URL to your KiwiSDRs status page here
# e.g. http://192.168.1.100:8073/status
export KIWISDR_URL=""
export KIWISDR_NAME="Public 1"


# InfluxDB Settings
export INFLUXDB_URL="http://localhost:8086"
export INFLUXDB_TOKEN=""
export INFLUXDB_ORG=""
export INFLUXDB_BUCKET=""
export INFLUXDB_MEASNAME="kiwisdr_status"

# Use a local venv if it exists
VENV_DIR=venv
if [ -d "$VENV_DIR" ]; then
    echo "Entering venv."
    source $VENV_DIR/bin/activate
fi

python3 kiwi_status.py
