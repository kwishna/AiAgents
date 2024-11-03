#! /bin/bash
x=888
y=999

# Addition
add()
{
    echo "$1 + $2 = $[$1+$2]"
}

# Multiplication
multiply()
{
    echo "$1 * $2 = $[$1*$2]"
}

# Subtraction
subtract()
{
    echo "$1 - $2 = $[$1-$2]"
}

# Division
divide()
{
    echo "$1 / $2 = $[$1/$2]"
}