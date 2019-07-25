#!/bin/bash

ls -lv s$1/1C_crop$1*.out > sorted.txt

sed -E 's/[ ]+/ /g' sorted.txt | cut -f 9 -d ' ' | xargs tail | grep 'val_loss' | cut -f 8 -d ' '

rm sorted.txt
