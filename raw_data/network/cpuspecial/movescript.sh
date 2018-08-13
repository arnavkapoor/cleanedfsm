mkdir -p cpuminimumsorted
for files in ./*
do
	refile=`basename $files`
	refile2=`echo $refile|cut -d "-" -f1`
	if [[ "$refile" != "$refile2" ]]
	then
		refile2="$refile2.csv" 
	fi
	if [ ${files: -4} == ".csv" ]
	then
		mv "$files" ./cpuminimumsorted/"$refile2"
	fi
done