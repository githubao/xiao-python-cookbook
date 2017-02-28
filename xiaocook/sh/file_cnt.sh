#!/usr/bin/env bash

for file in `ls`;do
if [ -d $file ];then
cd $file
echo -n $file
echo `ls | wc -l`
cd ..
fi
done