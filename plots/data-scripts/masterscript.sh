#!/bin/bash

python consolidated.py "$1" "$2" "$3"
python mergecsv.py
python splitcsv.py "$4"


# $1 cpuraw results
# $2 gpuraw results
# $3 0 - minimum 1 - maximum 	
# $4 folder to save the computed results

