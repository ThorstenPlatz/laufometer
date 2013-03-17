#!/bin/sh

PID_FILE="/var/run/laufometer/pid/laufometer.pid"

if [ ! -f $PID_FILE ];
then
    echo "Pidfile $PID_FILE not found!"
    exit 1
fi

PID="$(cat $PID_FILE)"
if [ "x$PIDx" = "xx" ];
then
    echo "No PID found!"
    exit 2
fi

CMD="kill -SIGINT $PID"

echo "stopping..."

sudo $CMD 

