#!/bin/sh
[ "`id -un`" != "whatever"  ] && exit 1
. ~/bot/bin/activate
sopel --fork
