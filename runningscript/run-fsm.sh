# outputs
resultsdir=$1
with_offsets=$2 #values 0 or 1
char=$3 #values 0 or 1
do_sort=$4 # values N or Y
cpuresults="$resultsdir/cpu"
gpuresults="$resultsdir/gpu"
output_file=run.out

# inputs
subjectroot=~/fsmtesting/cleanedfsm/subjects/network
testroot=~/fsmtesting/cleanedfsm/test_case_generation/transition_pair_tests
maxlengthsroot=~/fsmtesting/cleanedfsm/runningscript/maxlengths/

partecldir=~/partecl-runtime

for file in "$subjectroot"/*
do
  # get tne name of the subject fsm
  basenm=$(basename "$file")
  noextension=`echo "$basenm" | cut -d '.' -f1`

  # get the fsm attributes
  no_of_transitions=$((`cat "$file" | wc -l` - 5))
  no_of_states=$((`cat "$file" | head -3 | tail -1 | cut -d " " -f2` + 1))
  input=$((`cat "$file" | head -1 | cut -d " " -f 2` + 1))
  output=$((`cat "$file" | head -2 | tail -1 | cut -d " " -f 2` + 1))
  max_test_length=`cat "$maxlengthsroot/$basenm"`

  # copy the tests
  echo "Copy tests $basenm."
  cp "$testroot/$basenm" "$partecldir/kernel-gen/tests.txt"
  no_of_tests=`cat "$partecldir/kernel-gen/tests.txt" | wc -l`

  # set the constants
  sed -i "/#define INPUT_LENFTH_FSM /s/.*/#define INPUT_LENGTH_FSM ${input}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define OUTPUT_LENFTH_FSM /s/.*/#define OUTPUT_LENGTH_FSM ${output}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define NUM_STATES /s/.*/#define NUM_STATES ${no_of_states}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define PADDED_INPUT_ARRAY_SIZE /s/.*/#define PADDED_INPUT_ARRAY_SIZE ${max_test_length}/" "$partecldir/kernel-gen/structs.h"
  sed -i "/#define FSM_INPUTS_COAL_CHAR /s/.*/#define FSM_INPUTS_COAL_CHAR ${char}/" "$partecldir/source/constants.h"
  sed -i "/#define FSM_INPUTS_WITH_OFFSETS /s/.*/#define FSM_INPUTS_WITH_OFFSETS ${with_offsets}/" "$partecldir/source/constants.h"
  echo "//blank comment" >> "$partecldir/source/main-working.cl"

  # build
  echo "Build $basenm."
  make -C "$partecldir/build" clean &>> $output_file
  make -C "$partecldir/build" &>> $output_file

  # make cpu and gpu dirs
  mkdir -p "$cpuresults/$basenm"
  mkdir -p "$gpuresults/$basenm"

  test_sizes=( 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 )

  for size in "${test_sizes[@]}"
  do
    if [ $size -le $no_of_tests ] 
    then
      # check correctness
      echo "Checking results for $basenm ${size}..."
      is_correct=$(bash "$partecldir/scripts/compare-correctness.sh" $size $file 16 $do_sort 0 N)
    
      if [ "$is_correct" == "-1" ]
      then
        echo "NOT CORRECT!"
      else
        echo "CORRECT!" 
        echo "Running experiments for $basenm ${size}..."
        # run cpu results
        filesavecpu=""$size"_16_"$noextension".test"
        bash "$partecldir/build/openmp-run.sh" $size Y N 201 16 $file $do_sort > "$cpuresults/$basenm/$filesavecpu" 2>>$output_file

        # run gpu results
        filesavegpu=""$size"_"$noextension".test"
        "$partecldir/build/gpu-test" $size -time Y -results N -runs 201 -sort $do_sort -ldim 256 -filename $file > "$gpuresults/$basenm/$filesavegpu" 2>> $output_file
        echo "DONE!"
      fi
    fi
  done
  echo -e "\n"
done
