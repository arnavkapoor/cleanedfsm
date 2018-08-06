#!/bin/bash
FSM_DIRECTORY=$1 #directory conating the fsm's

mkdir -p prefix_list
mkdir -p transition_pairs
mkdir -p transition_pair_tests

for files in $FSM_DIRECTORY/*
do
	new=($(basename $files))
	echo $new
	python ./prefix-gen.py $files
	python ./transitionpair.py $files
	python ./better-testgen.py ./transition_pairs/$new ./prefix_list/$new
	cp ./transition_pair_tests/$new temp.txt
	cat temp.txt| shuf | cut -d " " -f 2 | nl -nln > ./transition_pair_tests/$new
	rm temp.txt
	sed -i -e "s/[[:space:]]\+/ /g" ./transition_pair_tests/$new
done
