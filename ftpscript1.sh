#!/bin/sh

HOST='10.0.2.15'
USER='dannyalmois'
PASSWD='115588'
FILE='test.html'

ftp -n $HOST <<END_SCRIPT
quote USER $USER
quote PASS $PASSWD
put $FILE
quit
END_SCRIPT
exit 0


