#!/bin/sh

# LSB-compliance meta information:

### BEGIN INIT INFO
# Provides:          laufometer
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start laufometer-client at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

OUT_FILE="/var/log/laufometer/laufometer.log"
PID_FILE="/var/run/laufometer/pid/laufometer.pid"

SCRIPT=$(which $0)
#SCRIPT_DIR=$(dirname $SCRIPT)
SCRIPT_DIR="/home/pi/laufometer/laufometer"

# text formatting options
RED="$(tput setaf 1)"
GREEN="$(tput setaf 2)"
RESET="$(tput sgr0)"

start() {
    CMD="sudo python3 $SCRIPT_DIR/main.py > $OUT_FILE 2>&1"
    # run as root, because GIPO access is only allowed for root
    sudo sh -c "$CMD" &
}

stop() {
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
}

status() {
    if [ -f $PID_FILE ];
    then
      PID="$(cat $PID_FILE)"
      if [ "x$PIDx" != "xx" ]; then
        if [ $(ps -p $PID | wc -l) = 2 ]; then
          echo "${GREEN}running with PID=$PID ${RESET}"
          exit 0
        fi
      fi
    fi

    echo "${RED}stopped${RESET}"
    exit 1
}

case "$1" in
  start)
    start
    sleep 3
    status
    ;;
  stop)
    stop
    sleep 3
    status
    ;;
  status)
    status
    ;;
  restart)
    stop
    sleep 3
    start
    sleep 3
    status
    ;;
  *)
    echo "Usage: $SCRIPT {start|stop|status}"
    exit 1
    ;;
esac

exit 0

