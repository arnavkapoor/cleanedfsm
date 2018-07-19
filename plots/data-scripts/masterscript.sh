#!/bin/bash

python consolidated.py "$1" "$2"
python mergecsv.py
python splitcsv.py "$3"


# $1 cpuraw results
# $2 gpuraw results
# $3 folder to save the computed results

