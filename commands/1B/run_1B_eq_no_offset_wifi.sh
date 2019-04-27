#!/bin/bash

# Script file to run Task 1B with equalized no offset wifi data.
# Inputs:
#   1: GPU id to use
#   2: directory to save results


mkdir -p $2'results/1B/equalized/wifi/phy_payload_no_offsets_iq/'

echo "Starting job"

python -u /home/bruno/RFMLS/train_val_framework/test_framework.py \
    --exp_name 1B_eq_no_offset_wifi \
    --base_path /scratch/RFMLS/dec18_darpa/v3_list/equalized/1Bv2/phy_payload_no_offsets_iq/ \
    --stats_path /scratch/RFMLS/dec18_darpa/v3_list/equalized/1Bv2/phy_payload_no_offsets_iq/ \
    --save_path /home/bruno/RFMLS/results/1B/equalized/wifi/phy_payload_no_offsets_iq/ \
    --file_type pickle \
    --model_flag baseline \
    --slice_size 256 \
    --devices 250 \
    --dropout_flag False \
    --fc_stack 3 \
    --cnn_stack 5 \
    --id_gpu $1 \
    --generator new \
    --add_padding True \
    --K 10 \
    --channels 128 \
    --training_strategy big \
    --batch_size 128 \
    --lr 0.0001 \
    --multigpu False \
    --normalize True \
    --train True \
    --test True \
    --epochs 5 \
    --batchnorm False \
    --early_stopping True \
    --patience 7 \
