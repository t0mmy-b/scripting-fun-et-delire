#!/bin/bash

##################################################
# 		                 ________   _____        #
# 		  _________  ___/  _____/  /  |  |       #
# 		 /  ___/\  \/  /   __  \  /   |  |_      #
# 	 A   \___ \  >    <\  |__\  \/    ^   / WORK #
# 		/____  >/__/\_ \\_____  /\____   |       #
# 		     \/       \/      \/      |__|       #
#												 #
##################################################
## contact: tbsx (at) outlook (dot) fr
## DO NOT FORGET TO RUN CHMOD 755 42-folder-creator.sh
## USAGE: ./42-folder-creator.sh

echo "You need to specify the path to create every folders. (Default: ./)"
printf 'Path: '
read path
echo "You must put a name to the main folder. (Default: '42-days')"
printf 'Main folder: '
read main

## DEFAULT CHECK
if [ ! $path ]; then
	path='.'
fi
if [ ! $main ]; then
	main='42-days'
fi

## MAIN AND SUB-FOLDERS CREATION
cd $path

if [ -d $main ]; then
	rm -rf $main
fi
mkdir $main

for (( i = 0; i < 14; i++ )); do
	if [ $i -lt 10 ]; then
		mkdir $main/Day0$i
	else
		mkdir $main/Day$i
	fi
done

cd $main

## BAD WRITTEN STUFF GOING HERE FUUUUCK

n=()
for (( i = 0; i < 14; i++ )); do
	if [ $i -lt 10 ]; then
		echo 'How many exercises are in Day0'$i
		printf '> '
		read n[$i]
		echo Entering Day0$i...
		cd Day0$i
	else
		echo 'How many exercises are in Day'$i
		printf '> '
		read n[$i]
		echo Entering Day$i
		cd Day$i
	fi
	for (( j = 0; j <= ${n[$i]} - 1; j++ )); do
		if [ $j -lt 10 ]; then
			echo Creating ex0$j...
			mkdir ex0$j
		else
			echo Creating ex$j...
			mkdir ex$j
		fi
	done
	echo Leaving...
	cd ..
done