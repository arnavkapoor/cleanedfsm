#!/bin/bash
FSM_DIRECTORY=$1 #directory conating the fsm's
mkdir -p prefix-list-network
mkdir -p transition-pairs-network
mkdir -p transition-pair-tests-network

for files in $FSM_DIRECTORY/*
do
	new=($(basename $files))
	echo $new
	python ./prefix-gen.py $files
	python ./transitionpairnetwork.py $files
	python ./better-testgen.py ./transition-pairs-network/$new ./prefix-list-network/$new
	cp ./transition-pair-tests-network/$new temp.txt
	cat temp.txt| shuf | cut -d " " -f 2 | nl -nln > ./transition-pair-tests-network/$new
	rm temp.txt
	sed -i -e "s/[[:space:]]\+/ /g" ./transition-pair-tests-network/$new
done