#!/bin/bash

#ls -lv $1/1C_crop$1*.out > /mnt/WDMyBook/sorted.txt
ls -lv /home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firbinarytest/*/log.out > /home/bruno/sorted.txt
sed -E 's/[ ]+/ /g' /home/bruno/sorted.txt | cut -f 9 -d ' ' | xargs tail -n 1 -q | cut -f 2 -d ' ' | cut -f 1 -d ')'
rm /home/bruno/sorted.txt
