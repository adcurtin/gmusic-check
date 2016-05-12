#!/bin/bash

pushd /Users/adcurtin/gmusic-playlist/ > /dev/null
rm -r previous
cp -r current previous
/usr/local/bin/python ExportLists.py current > export.log

diff current/All.csv previous/All.csv > All.diff

if [[ $? -ne 0 ]]
then
	egrep '>' All.diff > /dev/null
	changed=$?
	cat All.diff | /usr/local/bin/python sendemail.py $changed
# else
# 	echo "same"
fi
popd  > /dev/null
