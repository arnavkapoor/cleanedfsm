# padded 0 0
# padded-transposed 0 1
# with-offsets 1 0

# dense unsorted
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/unsorted/padded 0 0 N
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/unsorted/padded-transposed 0 1 N
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/unsorted/with-offsets 1 0 N

# dense sorted
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/sorted/padded 0 0 Y
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/sorted/padded-transposed 0 1 Y
./run-fsm.sh ~/fsmtesting/cleanedfsm/raw_data/20180806/denseresults/sorted/with-offsets 1 0 Y
