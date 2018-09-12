#!/bin/bash
FSM_DIRECTORY=$1 #directory conating the fsm's
OUTPUT_DIRECTORY=$2 #directory to save the test cases

mkdir -p "$OUTPUT_DIRECTORY/prefix_list"
mkdir -p "$OUTPUT_DIRECTORY/transition_pairs"
mkdir -p "$OUTPUT_DIRECTORY/transition_pair_tests"

for files in $FSM_DIRECTORY/*
do
        start1=`date +%s.%N`
	new=($(basename $files))
	echo $new
	python ./prefix-gen.py $files $OUTPUT_DIRECTORY
	python ./transitionpair.py $files $OUTPUT_DIRECTORY
	python ./better-testgen.py "$OUTPUT_DIRECTORY/transition_pairs/$new" "$OUTPUT_DIRECTORY/prefix_list/$new" $OUTPUT_DIRECTORY
	cp "$OUTPUT_DIRECTORY/transition_pair_tests/$new" temp.txt
	cat temp.txt| shuf | cut -d " " -f 2 | nl -nln > "$OUTPUT_DIRECTORY/transition_pair_tests/$new"
	rm temp.txt
	sed -i -e "s/[[:space:]]\+/ /g" "$OUTPUT_DIRECTORY/transition_pair_tests/$new"
        end=`date +%s.%N`

        runtime=$( echo "$end-$start1" | bc -l)
        echo "time $runtime seconds"
done
