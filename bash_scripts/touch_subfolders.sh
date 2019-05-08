#!/bin/bash

array=( $(ls .) )

for file in * ; do
    echo "$file"
    touch "$file/ADS-B/resnet1d/.keep"
    touch "$file/ADS-B/baseline/.keep"
    touch "$file/mixed/resnet1d/.keep"
    touch "$file/mixed/baseline/.keep"
    touch "$file/wifi/equalized/resnet1d/.keep"
    touch "$file/wifi/equalized/baseline/.keep"
    touch "$file/wifi/raw_samples/resnet1d/.keep"
    touch "$file/wifi/raw_samples/baseline/.keep"
done


#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/ADS-B/resnet1d
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/ADS-B/baseline
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/
#ADS-B/ mixed/ wifi/
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/mixed/resnet1d
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/mixed/baseline
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/wifi/
#equalized/   raw_samples/
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/wifi/equalized/resnet1d
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/wifi/equalized/baseline
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/wifi/raw_samples/resnet1d
#(base) bruno@rfmls-DGX-Station:~/Models$ mkdir 1Av2/wifi/raw_samples/baseline
#
