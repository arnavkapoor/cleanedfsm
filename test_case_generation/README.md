addmetadatanetwork.sh is the main script which takes the directory containing fsm's as the parameter.

prefix-gen.py - generates the list of inputs required to reach any state from the starting state. (the current state in the first line of the fsm) and saves the results in prefix-list-network


transition-pair-network.py
This generates the transition pair fsm from the transition fsm taking all possible pairs of inputs and saves in transition-pairs-network folder

transition-pair-tests-network 
using the transition-pairs-network fsm and the prefix-list-network generates the required test case.