#!/bin/sh

BASEDIR=`dirname $0`
if [ `uname` == "Darwin" ]; then
    $BASEDIR/mac_new_challenge.sh
else
    $BASEDIR/linux_new_challenge.sh
fi