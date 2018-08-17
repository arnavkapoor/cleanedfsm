# padded 0 0
# padded-transposed 0 1
# with-offsets 1 0

$base_folder=~/fsmtesting/cleanedfsm/raw_data/201808/denseresults
mkdir -p $base_folder

# dense unsorted
./run-fsm.sh "$base_folder/unsorted/padded" 0 0 N
./run-fsm.sh "$base_folder/unsorted/padded-transposed" 0 1 N
./run-fsm.sh "$base_folder/unsorted/with-offsets" 1 0 N

# dense sorted
./run-fsm.sh "$base_folder/sorted/padded" 0 0 Y
./run-fsm.sh "$base_folder/sorted/padded-transposed" 0 1 Y
./run-fsm.sh "$base_folder/sorted/with-offsets" 1 0 Y
