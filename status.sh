#!/bin/sh

PID_FILE="/var/run/laufometer/pid/laufometer.pid"

if [ -f $PID_FILE ];
then
    PID="$(cat $PID_FILE)"
    if [ "x$PIDx" != "xx" ];
    then
        if [ $(ps -p $PID | wc -l) = 2 ];
        then
            echo "running with PID=$PID"
            exit 0
        fi
    fi
fi


echo "stopped"
exit 1
