#!/bin/bash

ls -lv s$1/1C_crop$1*.out > /mnt/WDMyBook/sorted.txt
sed -E 's/[ ]+/ /g' /mnt/WDMyBook/sorted.txt | cut -f 9 -d ' ' | xargs tail -n 1 -q | cut -f 2 -d ' ' | cut -f 1 -d ')'
rm /mnt/WDMyBook/sorted.txt
