#!/bin/bash

./run.sh --task 1Cv2 \
         --train_tsv /scratch/RFMLS/RFML_Test_Specs_Delivered_v3/test1/1Cv2.train.tsv \
         --test_tsv /scratch/RFMLS/RFML_Test_Specs_Delivered_v3/test1/1Cv2.test.tsv \
         --root_wifi /mnt/rfmls_data/disk1/wifi_sigmf_dataset_gfi_1/ \
         --root_adsb /mnt/rfmls_data/disk2/adsb_gfi_3_dataset/ \
         --out_root_data /home/bruno/RFMLS/docker/data/test4/ \
         --out_root_list /home/bruno/RFMLS/docker/data/test4_list/ \
         --preprocess true \
         --framework false
