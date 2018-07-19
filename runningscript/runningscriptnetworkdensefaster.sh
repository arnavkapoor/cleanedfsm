#toggleoffset=$1
#charon=$2
#char4on=$3

#echo $toggleoffset
#echo $charon

#sed -i "/#define FSM_INPUTS_WITH_OFFSETS/s/.*/#define FSM_INPUTS_WITH_OFFSETS ${toggleoffset}/" ~/partecl-runtime/source/constants.h
#sed -i "/#define FSM_INPUTS_COAL_CHAR/s/.*/#define FSM_INPUTS_COAL_CHAR ${charon}/" ~/partecl-runtime/source/constants.h

savingnamecpu=$1
savingnamegpu=$2
sorting=$3
commonroot=~/fsmresults/newbeginning/network/allregexnew

for file in "$commonroot"/*
do
	echo $basenm
	basenm=$(basename "$file")
	noextension=`echo "$basenm"| cut -d '.' -f1`
 	
	no_of_transitions=`cat "/afs/inf.ed.ac.uk/user/v/v1akapoo/fsmresults/newbeginning/network/allregexnew/$basenm"|wc -l` 
	input=`cat "/afs/inf.ed.ac.uk/user/v/v1akapoo/fsmresults/newbeginning/network/allregexnew/$basenm" | head -1 | cut -d " " -f 2`
	output=`cat "/afs/inf.ed.ac.uk/user/v/v1akapoo/fsmresults/newbeginning/network/allregexnew/$basenm" | head -2 | tail -1 | cut -d " " -f 2` 	
	no_of_transitions=$((no_of_transitions-5))
	input=$((input+1))
	output=$((output+1))	
	no_of_states=`cat "/afs/inf.ed.ac.uk/user/v/v1akapoo/fsmresults/newbeginning/network/allregexnew/$basenm" | head -3 | tail -1 | cut -d " " -f 2`
	no_of_states=$((no_of_states+1))
		

	if [ $no_of_transitions -ne 0 ]
	then
		sed -i "/#define INPUT_LENGTH_FSM/s/.*/#define INPUT_LENGTH_FSM ${input}/" ~/partecl-runtime/kernel-gen/compile_const.h
		sed -i "/#define OUTPUT_LENGTH_FSM/s/.*/#define OUTPUT_LENGTH_FSM ${output}/" ~/partecl-runtime/kernel-gen/compile_const.h
		sed -i "/#define NUM_STATES/s/.*/#define NUM_STATES ${no_of_states}/" ~/partecl-runtime/kernel-gen/compile_const.h
		
		echo "// blank comment" >> ~/partecl-runtime/source/main-working.cl	
		
		cd ~/fsmresults/newbeginning/network/swiftsidecode
		#bash addmetadatanetwork.sh $basenm 
	
		op=`cat "maxlengthsfsm/$basenm"`
    		
		#op=`python maxinputlengthnew.py $basenm`
		echo "max len is $op"
		
		cd -
		sed -i  "/#define PADDED_INPUT_ARRAY_SIZE/s/.*/#define PADDED_INPUT_ARRAY_SIZE ${op}/" ~/partecl-runtime/kernel-gen/structs.h
		
		
		no_of_tests=`cat ~/fsmresults/newbeginning/network/swiftsidecode/transition-pair-tests-network/"$basenm" | wc -l`
		
		echo $no_of_tests	
		echo $no_of_states
		echo $basenm
		echo $input
		echo $output	
			
		mkdir -p ~/$savingnamecpu/$basenm
		mkdir -p ~/$savingnamegpu/$basenm	
		
		#rm ~/fsmresults/newbeginning/network/swiftsidecode/transition-pairs-network/"$basenm"	
		cp ~/fsmresults/newbeginning/network/swiftsidecode/transition-pair-tests-network/"$basenm" ~/partecl-runtime/kernel-gen/tests.txt	
		 
		make -C ~/partecl-runtime/build clean
		make -C ~/partecl-runtime/build
	
		if [ 2048 -le $no_of_tests  ]  
		then	
			filesave="2048_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2048 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
				
			filesave="2048_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2048 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="2048_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2048 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="2048_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2048 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="2048_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 2048 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi		
	
                if [ 4096 -le $no_of_tests ]
                then
                
			filesave="4096_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="4096_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="4096_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="4096_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4096 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="4096_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 4096 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi

                if [ 8192 -le $no_of_tests ]
                then
                
			filesave="8192_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 8192 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="8192_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 8192 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="8192_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 8192 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="8192_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 8192 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="8192_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 8192 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
                if [ 16384 -le $no_of_tests ]
                then
                
			filesave="16384_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="16384_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="16384_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="16384_32_"$noextension".test"
		
			bash ~/partecl-runtime/build/openmp-run.sh 16384 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="16384_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 16384 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi		
			
                if [ 32768 -le $no_of_tests ]
                then
                
			filesave="32768_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 32768 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="32768_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 32768 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="32768_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 32768 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="32768_32_"$noextension".test"
		
			bash ~/partecl-runtime/build/openmp-run.sh 32768 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="32768_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 32768 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
	
                if [ 65536 -le $no_of_tests ]
                then
                
			filesave="65536_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="65536_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="65536_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="65536_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 65536 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="65536_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 65536 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi		
		
                if [ 131072 -le $no_of_tests ]
                then
		
			filesave="131072_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="131072_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="131072_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="131072_32_"$noextension".test"
         		
			bash ~/partecl-runtime/build/openmp-run.sh 131072 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="131072_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 131072 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi

		
		if [ 262144 -le $no_of_tests ]
                then
                
			filesave="262144_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 262144 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="262144_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 262144 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="262144_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 262144 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="262144_32_"$noextension".test"
		
			bash ~/partecl-runtime/build/openmp-run.sh 262144 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="262144_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 262144 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
		
                if [ 524288 -le $no_of_tests ]
                then
                
			filesave="524288_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 524288 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="524288_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 524288 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="524288_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 524288 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="524288_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 524288 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
		
			
			filesave="524288_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 524288 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi

                if [ 1048576 -le $no_of_tests ]
                then
                
			filesave="1048576_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 1048576 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="1048576_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 1048576 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="1048576_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 1048576 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="1048576_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 1048576 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="1048576_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 1048576 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
			
                if [ 2097152 -le $no_of_tests ]
                then
                
			filesave="2097152_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2097152 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="2097152_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2097152 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="2097152_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2097152 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="2097152_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 2097152 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="2097152_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 2097152 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
			
                if [ 4194304 -le $no_of_tests ]
                then
                
			filesave="4194304_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4194304 Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="4194304_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4194304 Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="4194304_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh 4194304 Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave="4194304_32_"$noextension".test"	
			bash ~/partecl-runtime/build/openmp-run.sh 4194304 Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave="4194304_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test 4194304 -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave
		
		fi
		
			filesave=""$no_of_tests"_1_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 101 1 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave=""$no_of_tests"_16_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 101 16 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			 
			filesave=""$no_of_tests"_8_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 101 8 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			  
			filesave=""$no_of_tests"_32_"$noextension".test"
			bash ~/partecl-runtime/build/openmp-run.sh $no_of_tests Y N 101 32 "$commonroot"/"$basenm" $sorting > ~/$savingnamecpu/$basenm/$filesave  	
			
			filesave=""$no_of_tests"_"$noextension".test"  		
			~/partecl-runtime/build/gpu-test $no_of_tests -time Y -results N -runs 101 -sort $sorting -ldim 256 -filename "$commonroot"/"$basenm" > ~/$savingnamegpu/$basenm/$filesave		

		#rm ~/fsmresults/newbeginning/network/swiftsidecode/transition-pair-tests-network/"$basenm"
	fi
#	fi
done
