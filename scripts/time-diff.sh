#!/bin/bash

if [ $# -lt 1 ] ; then
  echo "usage  : $0 <test time> [<reference time>]"
  echo "example: $0 \"2013-01-31T18:00:00\""
  exit -1
fi

if [ $# -gt 1 ] ; then
  REF_TIME="$(date --date='$2' '+%s')"
else
  REF_TIME=$(date "+%s")
fi

TEST_TIME=$(date --date="$1" "+%s")

DIFF=$(( $REF_TIME - $TEST_TIME ))

#echo "REF_TIME: $REF_TIME"
#echo "TEST_TIME: $TEST_TIME"

echo "$DIFF"

