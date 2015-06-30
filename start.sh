#!/bin/bash
set -e

CONF=/etc/car-monitoring-web-api/car-monitoring-web-api.conf

exec /usr/local/bin/car-monitoring-web-api
