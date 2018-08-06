tests_dir_root=$1
maxlengths_dir_root=maxlengths

mkdir -p $maxlengths_dir_root

for file in "$tests_dir_root"/*
do
  basenm=$(basename "$file")
  echo $basenm

  maxlength=`python maxinputlengthnew.py $file` 
  echo $maxlength
  echo $maxlength > "$maxlengths_dir_root/$basenm"
done
