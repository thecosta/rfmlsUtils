#!/bin/bash
exp='test_load_params'
python -u /home/bruno/RFMLS/docker/src/train_val_framework/test_framework.py \
   --exp_name $exp \
   --base_path /scratch/RFMLS/dec18_darpa/v3_list/raw_samples/1Av2/wifi/ \
   --stats_path /scratch/RFMLS/dec18_darpa/v3_list/raw_samples/1Av2/wifi/ \
   --save_path /home/bruno/docker_test/ \
   --file_type mat \
   --model_flag baseline \
   --rsp /home/bruno/RFMLS/Models/1Cv2/wifi/raw_samples/baseline/params.config \
   --slice_size 198 \
   --batch_size 128 \
   --epochs 20 \
   --patience 10 \
   --lr 0.0001 \
   --devices 500 \
   --fc_stack 2 \
   --cnn_stack 5 \
   --id_gpu $1 \
   --generator new \
   --channels 128 \
   --train False \
   --test False \
