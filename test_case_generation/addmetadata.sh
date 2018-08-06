#!/bin/bash
FSM_DIRECTORY=$1 #directory conating the fsm's

mkdir -p prefix-list
mkdir -p transition-pairs
mkdir -p transition-pair-tests

for files in $FSM_DIRECTORY/*
do
	new=($(basename $files))
	echo $new
	python ./prefix-gen.py $files
	python ./transitionpair.py $files
	python ./better-testgen.py ./transition-pairs/$new ./prefix-list/$new
	cp ./transition-pair-tests/$new temp.txt
	cat temp.txt| shuf | cut -d " " -f 2 | nl -nln > ./transition-pair-tests/$new
	rm temp.txt
	sed -i -e "s/[[:space:]]\+/ /g" ./transition-pair-tests/$new
done
