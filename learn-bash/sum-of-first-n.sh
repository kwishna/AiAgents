#! /bin/bash
read -p "Enter n value: " n

i=1
sum=0

while [ $i -le $n ]
do
    let sum=sum+i
    let i++
done
echo "The Sum of first $n numbers: $sum"