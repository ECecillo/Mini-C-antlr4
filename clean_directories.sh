#!/bin/sh

./TP02/ariteval/ && make clean \
  ./TP02/demo_files/ex1/ && make clean \
  ./TP02/demo_files/ex2/ && make clean \
  ./TP02/demo_files/ex4/ && make clean \
  ./TP02/demo_files/ex5/ && make clean

echo "Finished cleaning antlr generated files."
