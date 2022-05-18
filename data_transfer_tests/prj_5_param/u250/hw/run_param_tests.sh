#!/bin/bash

for (( i = 100000; i<= 1000000; i+=5000))
do
  rm app.exe
  make app.exe -j
  ./app.exe $i

done
