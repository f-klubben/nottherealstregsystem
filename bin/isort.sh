#!/usr/bin/env bash

o=$(isort -rc -cs -s migrations --diff stregsystem)
echo "${o}"
size=${#o}
if [ "${size}" != 0 ]; then
    exit 1
fi
