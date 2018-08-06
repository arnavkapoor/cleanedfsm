# outputs
resultsdir=$1
do_sort=$2
with_offsets=$3
char=$4
cpuresults="$resultsdir/cpu"
gpuresults="$resultsdir/gpu"

#TODO: Add test layout consts and sorting

# inputs
subjectroot=~/fsmtesting/cleanedfsm/subjects
testroot=~/fsmtesting/cleanedfsm/test_case_generation/transition_pair_tests
maxlengthsroot=~/fsmtesting/cleanedfsm/runningscript/maxlengths

partecldir=~/partecl-runtime

for file in "$subjectroot"/*
do
  # get tne name of the subject fsm
  basenm=$(basename "$file")
  noextension=`echo "$basenm" | cut -d '.' -f1`

  # get the fsm attributes
  no_of_transitions=$((`cat "$file" | wc -l` - 5))
  no_of_states=`cat "$file" | head -3 | tail -1 | cut -d " " -f2`
  input=$((`cat "$file" | head -1 | cut -d " " -f 2` + 1))
  output=$((`cat "$file" | head -2 | tail -1 | cut -d " " -f 2` + 1))
  max_test_length=`cat "$maxlengthsroot/$basenm"`
  echo $max_test_length

  # copy the tests
  echo "copying tests $basenm"
  cp "$testroot/$basenm" "$partecldir/kernel-gen/tests.txt"
  no_of_tests=`cat "$partecldir/kernel-gen/tests.txt" | wc -l`
  echo $no_of_tests

  # set the constants
  sed -i "/#define INPUT_LENFTH_FSM/s/.*/#define INPUT_LENGTH_FSM ${input}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define OUTPUT_LENFTH_FSM/s/.*/#define OUTPUT_LENGTH_FSM ${output}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define NUM_STATES/s/.*/#define NUM_STATES ${no_of_states}/" "$partecldir/kernel-gen/compile_const.h"
  sed -i "/#define PADDED_INPUT_ARRAY_SIZE/s/.*/#define PADDED_INPUT_ARRAY_SIZE ${max_test_length}/" "$partecldir/kernel-gen/structs.h"
  sed -i "/#define FSM_INPUTS_COAL_CHAR/s/.*/#define FSM_INPUTS_COAL_CHAR ${char}/" "$partecldir/source/constants.h"
  sed -i "/#define FSM_INPUTS_WITH_OFFSETS/s/.*/#define FSM_INPUTS_WITH_OFFSETS ${with_offsets}/" "$partecldir/source/constants.h"
  echo "//blank comment" >> "$partecldir/source/main-working.cl"

  # build
  echo "building $basenm"
  make -C "$partecldir/build" clean
  make -C "$partecldir/build"

  # run cpu
  mkdir -p "$cpuresults/$basenm"

  if [ 2048 -le $no_of_tests ] 
  then
    filesave="2048_16_"$noextension".test"
    bash "$partecldir/build/openmp-run.sh" 2048 Y N 201 16 "$file" N > "$cpuresults/$basenm/$filesave"
  fi

  # run gpu
  mkdir -p "$gpuresults/$basenm"

done
