#!/bin/sh
[ "`id -un`" -ne "whatever"  ] && exit 1
. bin/activate
sopel --fork
