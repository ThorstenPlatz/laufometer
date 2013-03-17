#!/bin/sh

OUT_FILE="/var/log/laufometer/laufometer.log"

SCRIPT=$(which $0)
SCRIPT_DIR=$(dirname $SCRIPT)

CMD="sudo python3 $SCRIPT_DIR/main.py > $OUT_FILE 2>&1"

sudo sh -c "$CMD" &

