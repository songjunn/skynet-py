#!/bin/sh

pwdpath=$(pwd)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pwdpath}

rm -rf ./*.py

#./protoc --python_out=../message *.proto
for i in ./*.proto
do
    ./protoc -I=. --python_out=../message $i
    if [ "$?" -eq 0 ]
    then
        echo $i
    else
        exit 1
    fi
done

