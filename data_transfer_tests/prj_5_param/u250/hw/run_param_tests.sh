#!/bin/bash

for (( i = 100000; i<= 1000000000; i+=5555500))
do
  rm app.exe
  make app.exe -j
  ./app.exe $i

done
