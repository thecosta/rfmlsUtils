import os
import h5py
import glob
import numpy as np
from scipy.io import loadmat, savemat
from FIRConv import FIRConv
from tqdm import tqdm

paths = glob.glob('/home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit2/*/1C_raw_wifi/')

devices = glob.glob('/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/*/*/')
new_datasets = '/scratch/bruno/RFMLS/dec18_darpa/v3/1Cv2/wifi_fir/'

datasets_list = '/scratch/bruno/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/'
new_datasets_list = '/scratch/bruno/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi_fir/'

ntaps = 5

kernel_real = np.random.normal(loc=0, scale=1.0/(2*ntaps), size=ntaps)
kernel_img = np.random.normal(loc=0, scale=1.0/(2*ntaps), size=ntaps)

kernel = np.transpose(np.stack((kernel_real, kernel_img)))

#for idx, _ in enumerate(kernel_real):
#    kernel[idx] = kernel_real[idx]+kernel_img[idx]*1j


for device in tqdm(devices):
    examples = glob.glob(device+'*')

    for example in examples:
        dirs = example.split('/')
        mfr = dirs[-3]
        device = dirs[-2]
        ex_name = dirs[-1]        

        if 'W' not in ex_name:
            continue

        mat_file = loadmat(example)
        new_mat_file = dict()
        
        for key in mat_file:
            if key != 'complexSignal':
                new_mat_file[key] = mat_file[key]

            else:
                X = mat_file[key]
                X = X.squeeze(0)
                X_real = np.zeros(shape=len(X))
                X_img = np.zeros(shape=len(X))

                for idx, pair in enumerate(X):
                    real = pair.real
                    img = pair.imag
                    X_real[idx] = real
                    X_img[idx] = img            
                X = np.transpose(np.stack((X_real, X_img)))
                X_fir = FIRConv(X, kernel)
                X_fir_real = X_fir[:, 0]
                X_fir_img = X_fir[:, 1]
                X_fir = X_fir_real + X_fir_img[idx] * 1j
                X_fir = np.expand_dims(X_fir, 0)
                
                new_mat_file[key] = X_fir

        save_dir = os.path.join(new_datasets, mfr, device)    
        save_path = os.path.join(new_datasets, mfr, device, ex_name)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        savemat(save_path, new_mat_file)
        







