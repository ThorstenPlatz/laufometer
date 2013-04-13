#!/bin/bash

TICK_LOGS="/var/log/laufometer/event-logs/"

if [ $# -lt 1 ] ; then
  echo "usage  : $0 <ALLOWED TIME DIFF IN SECONDS>"
  echo "example: $0 60"
  exit -1
fi

MAX_DIFF="$1"


SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $TICK_LOGS
LAST_ACTION=$(tail -n 1 $(ls -1t | head -n 1))
#echo "LAST_ACTION: $LAST_ACTION"

TIME_DIFF=$($SCRIPT_DIR/time-diff.sh "$LAST_ACTION")

#echo "TIME_DIFF: $TIME_DIFF"

if [ "$TIME_DIFF" -lt "$MAX_DIFF" ]; then
  echo "running"
  exit 0
else
  echo "idle"
  exit 1
fi

