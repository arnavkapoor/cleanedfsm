`addmetadatanetwork.sh` runs everything in order - it takes the directory containing fsm's as a parameter.

`prefix-gen.py` generates the list of inputs required to reach any state from the starting state and saves the results in `prefix-list-network`.

`transition-pair-network.py` generates the transition pair fsm from the transition fsm and saves in `transition-pairs-network`. 

`better-testgen.py`, generates the required test case inside `transition-pair-tests-network`; takes two parameters: 
  1. the `transition-pairs-network` folder 
  2. the `the prefix-list-network` folder 
