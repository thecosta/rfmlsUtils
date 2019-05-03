#!/bin/bash
#SBATCH --nodes=1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=multigpu
#SBATCH --mem=500Gb
#SBATCH --gres="gpu:8"
#SBATCH --export=ALL
#SBATCH --time=24:00:00
echo "Start JOB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#module load cuda/9.0
#module load python/2.7.15

mkdir -p /home/bruno/results/3E/wifi/equalized/resnet1d/

python -u /home/bruno/RFMLS/train_val_framework/test_framework.py \
    --exp_name 3E_wifi_equalized_resnet1d \
    --base_path /scratch/RFMLS/dec18_darpa/v4_list/equalized/3E \
    --stats_path /scratch/RFMLS/dec18_darpa/v4_list/equalized/3E \
    --save_path /home/bruno/results/3E/wifi/equalized/resnet1d/ \
    --devices 65 \
    --file_type pickle \
    --model_flag resnet1d \
    --slice_size 128 \
    --batchnorm False \
    --batch_size 64 \
    --add_padding True \
    --lr 0.0001 \
    --K 16 \
    --epochs 5 \
    --normalize True \
    --generator new \
    --training_strategy big \
    --multigpu False \
    --id_gpu $1 \
    --train True \
    --test True \
    --patience 10 \
    --channels 128 \
    --fc1 256 \
    --fc2 128 \
    --cnn_stack 5 \
    --dropout_flag False \
    --early_stopping True \
    --test_stride 16 \
    --fc_stack 2 \
    --decay 0.0 \
    --shrink 1 \
    > /home/bruno/results/3E/wifi/equalized/resnet1d/log.out \
    2> /home/bruno/results/3E/wifi/equalized/resnet1d/log.err
