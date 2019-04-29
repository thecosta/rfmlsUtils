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

mkdir -p /home/bruno/results/3Cv2/wifi/equalized/baseline/

python -u /home/bruno/RFMLS/train_val_framework/test_framework.py \
    --exp_name 3Cv2_wifi_equalized_baseline \
    --base_path /scratch/RFMLS/dec18_darpa/v3_list/equalized/3Cv2/phy_payload_no_offsets_iq/ \
    --stats_path /scratch/RFMLS/dec18_darpa/v3_list/equalized/3Cv2/phy_payload_no_offsets_iq/ \
    --save_path /home/bruno/results/3Cv2/wifi/equalized/baseline/ \
    --devices 100 \
    --file_type pickle \
    --model_flag baseline \
    --slice_size 256 \
    --batchnorm False \
    --batch_size 128 \
    --add_padding True \
    --lr 0.0005 \
    --K 16 \
    --epochs 10 \
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
    --test_stride 1 \
    --fc_stack 2 \
    --decay 0.0 \
    --shrink 1 \
    > /home/bruno/results/3Cv2/wifi/equalized/baseline/log.out \
    2> /home/bruno/results/3Cv2/wifi/equalized/baseline/log.err
