mkdir -p cpuminimumsorted
for files in ./*
do
	if [ ${files: -4} == ".csv" ]
	then
		mv "$files" ./cpuminimumsorted/
	fi
done