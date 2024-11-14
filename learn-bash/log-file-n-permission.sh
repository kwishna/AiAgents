#! /bin/bash
files=($(ls $(pwd)))
for fname in ${files[@]}
do
    echo -ne "$fname:\t\t"
    if [ -r $fname ]; then
        echo -ne "READ(Y)\t"
    else
        echo -ne "READ(N)\t"
    fi
    
    if [ -w $fname ]; then
        echo -ne "WRITE(Y)\t"
    else
        echo -ne "WRITE(N)\t"
    fi
    
    if [ -x $fname ]; then
        echo "EXECUTE(Y)"
    else
        echo "EXECUTE(N)"
    fi
done