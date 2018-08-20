
# padded 0 0
# padded-transposed 0 1
# with-offsets 1 0

base_folder="$HOME/fsmtesting/cleanedfsm/raw_data/201808/denseresults"

mkdir -p $base_folder

# dense unsorted
echo "Unsorted padded"
./run-fsm.sh "$base_folder/unsorted/padded" 0 0 N
echo "Unsorted padded-transposed"
./run-fsm.sh "$base_folder/unsorted/padded-transposed" 0 1 N
echo "Unsorted with-offsets"
./run-fsm.sh "$base_folder/unsorted/with-offsets" 1 0 N

# dense sorted
echo "Sorted padded"
./run-fsm.sh "$base_folder/sorted/padded" 0 0 Y
echo "Sorted padded-transposed"
./run-fsm.sh "$base_folder/sorted/padded-transposed" 0 1 Y
echo "Sorted with-offsets"
./run-fsm.sh "$base_folder/sorted/with-offsets" 1 0 Y
