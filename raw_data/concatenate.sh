#!/bin/bash
a="$(pwd)/$1" #first folder
b="$(pwd)/$2" #second folder
c="$(pwd)/$3" #result folder

(cd $a && find . -type f -name '*.test') |
while read file
do    
  mkdir -p "$c/$(dirname $file)"
  ( cat "$a/$file"
    [ -f "$b/$file" ] && sed '1,10d' < "$b/$file"
  ) >"$c/$file"
done
