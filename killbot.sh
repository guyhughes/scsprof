#!/bin/sh
[ "`id -un`" != "whatever"  ] && printf "run me as an unprivileged user!" && exit 1
. ~/bot/bin/activate
sopel -k
