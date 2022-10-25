#!/usr/bin/bash

#!(1)
echo -e "Please type a path: \c"

#!(2)
read path_utype
echo "The path you type (double check) :$path_utype"

#!(3)
nfl=0
ndr=0
for f in $(ls $path_utype); do
	if [ -d "$path_utype/$f" ];
	then
		ndr=$((ndr+1))
	else
		nfl=$((nfl+1))
	fi
done

echo "number of files = $nfl"
echo "number of directories = $ndr"


