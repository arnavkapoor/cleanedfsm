raw_data_folder_base=$1
results_folder_base=$2
min_or_median=$3 # 0 - min, 1 - median

# sorted
mkdir -p "$results_folder_base/sorted/padded"
./masterscript.sh "$raw_data_folder_base/sorted/padded/cpu" "$raw_data_folder_base/sorted/padded/gpu" $min_or_median "$results_folder_base/sorted/padded"

mkdir -p "$results_folder_base/sorted/padded-transposed"
./masterscript.sh "$raw_data_folder_base/sorted/padded-transposed/cpu" "$raw_data_folder_base/sorted/padded-transposed/gpu" $min_or_median "$results_folder_base/sorted/padded-transposed"

mkdir -p "$results_folder_base/sorted/with-offsets"
./masterscript.sh "$raw_data_folder_base/sorted/with-offsets/cpu" "$raw_data_folder_base/sorted/with-offsets/gpu" $min_or_median "$results_folder_base/sorted/with-offsets"

# unsorted
mkdir -p "$results_folder_base/unsorted/padded"
./masterscript.sh "$raw_data_folder_base/unsorted/padded/cpu" "$raw_data_folder_base/unsorted/padded/gpu" $min_or_median "$results_folder_base/unsorted/padded"

mkdir -p "$results_folder_base/unsorted/padded-transposed"
./masterscript.sh "$raw_data_folder_base/unsorted/padded-transposed/cpu" "$raw_data_folder_base/unsorted/padded-transposed/gpu" $min_or_median "$results_folder_base/unsorted/padded-transposed"

mkdir -p "$results_folder_base/unsorted/with-offsets"
./masterscript.sh "$raw_data_folder_base/unsorted/with-offsets/cpu" "$raw_data_folder_base/unsorted/with-offsets/gpu" $min_or_median "$results_folder_base/unsorted/with-offsets"
