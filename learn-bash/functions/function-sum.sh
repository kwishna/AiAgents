#! /bin/bash
sum()
{   
    # echo "passed variables $#"
    if [ $# != 2 ]; then
        echo "You should pass exactly two numbers."
        return 1
    else
        echo "The SUM is: $(($1+$2))"
    fi
}

sum $*