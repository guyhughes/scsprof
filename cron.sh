#!/bin/sh
SCRIPTNAME="$0"
if !( ps u | grep sopel | grep -v 'grep' >/dev/null 2>/dev/null ); then
	printf "starting up the sopel\n"
	exec $(dirname "$SCRIPTNAME")/startbot.sh
else
	printf "already running\n"
	return 0
fi 
