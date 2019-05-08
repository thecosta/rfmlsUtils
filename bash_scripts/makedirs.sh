#!/bin/bash

array=( $(ls .) )

for file in * ; do
    echo "$file"
    mkdir -p "$file/ADS-B/resnet1d"
    mkdir -p "$file/ADS-B/baseline"
    mkdir -p "$file/mixed/resnet1d"
    mkdir -p "$file/mixed/baseline"
    mkdir -p "$file/wifi/equalized/resnet1d"
    mkdir -p "$file/wifi/equalized/baseline"
    mkdir -p "$file/wifi/raw_samples/resnet1d"
    mkdir -p "$file/wifi/raw_samples/baseline"
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
