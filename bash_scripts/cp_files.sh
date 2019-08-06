#!/bin/bash

v3=$(ls /scratch/RFMLS/dec18_darpa/v3_list/raw_samples/)
v4_raw=$(ls /scratch/RFMLS/dec18_darpa/v4_list/raw_samples/)
v4_eq=$(ls /scratch/RFMLS/dec18_darpa/v4_list/equalized/)

for task in $v3; do
    echo "$task"
    cp /scratch/RFMLS/dec18_darpa/v3_list/raw_samples/$task/wifi/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/wifi/raw_samples/
    cp /scratch/RFMLS/dec18_darpa/v3_list/raw_samples/$task/ADS-B/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/ADS-B/
    cp /scratch/RFMLS/dec18_darpa/v3_list/equalized/$task/phy_payload_no_offsets_iq/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/wifi/equalized/ 
done

for task in $v4_raw; do
    echo $task
    cp /scratch/RFMLS/dec18_darpa/v4_list/raw_samples/$task/wifi/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/wifi/raw_samples/
    cp /scratch/RFMLS/dec18_darpa/v4_list/raw_samples/$task/ADS-B/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/ADS-B/
    cp /scratch/RFMLS/dec18_darpa/v4_list/equalized/$task/wifi/device_ids.pkl /home/bruno/RFMLS/docker/Models/$task/wifi/equalized/
done





