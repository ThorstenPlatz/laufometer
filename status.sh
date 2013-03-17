#!/bin/sh

PID_FILE="/var/run/laufometer/pid/laufometer.pid"

RED="$(tput setaf 1)"
GREEN="$(tput setaf 2)"
RESET="$(tput sgr0)"


if [ -f $PID_FILE ];
then
    PID="$(cat $PID_FILE)"
    if [ "x$PIDx" != "xx" ];
    then
        if [ $(ps -p $PID | wc -l) = 2 ];
        then
            echo "${GREEN}running with PID=$PID ${RESET}"
            exit 0
        fi
    fi
fi


echo "${RED}stopped${RESET}"
exit 1
