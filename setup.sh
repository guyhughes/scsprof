#!/bin/sh
virtualenv -p python2.7 ~/bot
. ~/bot/bin/activate
pip install sopel ipython
printf ""
printf "Okay I'm done. You can run ./startbot.sh now."
