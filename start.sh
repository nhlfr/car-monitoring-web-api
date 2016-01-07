#!/bin/bash
set -e

CONF=/etc/car-monitoring-web-api/car-monitoring-web-api.conf

sudo chown -R obd: /opt/car-monitoring-web-api

exec /var/lib/car-monitoring/venv/bin/car-monitoring-web-api
