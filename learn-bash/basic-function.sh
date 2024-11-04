#!/bin/bash
f1()
{
    echo "I am in f1 function"
}

f2()
{
    echo "I am in f2 function"
    f1
}

f1
f2