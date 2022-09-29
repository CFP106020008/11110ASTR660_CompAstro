#!/bin/bash

echo -e "Path: "
read path

let num_f=0
let num_d=0

for ff in $(ls $path); do
    if [ -f $path/$ff ]; then 
        echo "$ff is a file"
        ((num_f++))
    else [ -d $path/$ff ]; 
        echo "$ff is a dir"
        ((num_d++))
    fi
done

echo "There are $num_f files and $num_d directories."


