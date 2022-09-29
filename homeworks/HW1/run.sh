#!/bin/bash

echo -e "Path: "
read word

let count_f=0
let count_d=0

for ff in $(ls $word); do
    if [ -f $word/$ff ]; then 
        echo "$ff is a file"
        ((count_f++))
    else [ -d $word/$ff ]; 
        echo "$ff is a dir"
        ((count_d++))
    fi
done

echo "There are $count_f files and $count_d directories."


