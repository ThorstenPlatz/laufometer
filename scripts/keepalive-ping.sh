#!/bin/bash

KEEPALIVE_URL="http://laufometer.appspot.com/api/rest/public/watchdog/keepalive?clientId=paul-dsungi"

if [ $(/etc/init.d/laufometer status | grep "running with PID" | wc -l) -eq 1 ]; then 
  # send keepalive ping
  wget --quiet --spider $KEEPALIVE_URL
  echo "keepalive ping sent"
  exit 0
else
  echo "no keepalive ping sent"
  exit 1
fi
