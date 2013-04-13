#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $SCRIPT_DIR/settings.sh

if [ $# -lt 1 ] ; then
  cd $TICK_LOGS
  CURRENT_TICK_FILE=$(ls -1t | head -n 1)
else 
  CURRENT_TICK_FILE="$1"
fi

TICKS=$(cat $CURRENT_TICK_FILE)
CMD="curl --data-urlencode ticks@$CURRENT_TICK_FILE $TICK_IMPORT_URL"

#echo "CMD: $CMD"
$CMD

exit 0
