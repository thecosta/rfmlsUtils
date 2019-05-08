#!/bin/bash

echo "starting"
./run.sh --task 1Cv2 \
         --preprocess false \
         --framework true \
         --exp_name 1Cv2_baseline \
         --base_path /home/bruno/RFMLS/docker/data/test4_list/1Cv2/wifi\
         --stats_path /home/bruno/RFMLS/docker/data/test4_list/1Cv2/wifi \
         --save_path ./results/raw_samples/1Cv2/wifi
