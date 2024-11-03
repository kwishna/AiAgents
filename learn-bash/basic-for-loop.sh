#! /bin/bash

# Q9) Write a Script to Display all File Names Present in CurrentWorking Directory?
for name in *
do
    if [ -f $name ]; then
        echo $name
    fi
done