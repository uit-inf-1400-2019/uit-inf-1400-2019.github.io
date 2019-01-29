#!/bin/bash

for i in *.py
do
    echo "---------------------"
    echo $i
    echo "---------------------"
    python3 $i
done
