import os
import glob
import pickle
import numpy as np


device_paths = glob.glob('/home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_ensemble/*')

ensemble = {}

# Iterate over device paths
for device_path in device_paths:

    pred_files = glob.glob(device_path + '/*/1C_raw_wifi/preds.pkl')    
    tot_prob = np.array([50,])
    # Iterate over all predictions of weights tested on device
    for pred_file in pred_files:

        #print(preds)
        device_n = int(pred_file.split('/')[-4])
        weight_n = int(pred_file.split('/')[-3])

        real_label = device_n # before this was weight_n

        total_examples = 0
        correct_examples = 0
        #tot_prob = np.array([50,])
        with open(pred_file, 'r') as f:
            preds_pkl = pickle.load(f)
            device_acc = 0

            for pred in preds_pkl['preds_exp']:

                pred = preds_pkl['preds_exp'][pred]
                tot_prob = tot_prob+pred
                '''
                total_examples += 1
                predicted_class = np.argmax(pred)
                #print 'device: ', device_n, ', ', 'weight: ', weight_n, 'predicted: ', predicted_class
                #print(pred)
                #if total_examples == 100:
                #    a

                if predicted_class == int(real_label) and predicted_class == device_n :
                    #print 'device: ', device_n, ', ', 'weight: ', weight_n, 'predicted: ', predicted_class
                    correct_examples += 1
                

            acc = correct_examples*1.0 / total_examples

            if device_n not in ensemble:
                ensemble[device_n] = [(weight_n, acc)]
            else:
                ensemble[device_n].append((weight_n, acc))
            '''
    predicted_class = np.argmax(tot_prob)
    if device_n == 0:
        print tot_prob
    ensemble[device_n] = predicted_class

print ensemble

#a
'''
n = np.array(ensemble[6], dtype=[('device', int), ('acc', float)])
n = np.sort(n, order='device')

correct = 0
for device_class in ensemble:
    highest_class = 0
    highest_prob = 0
    for t in ensemble[device_class]:
        if t[1] > highest_prob:
            highest_class = t[0]
            highest_prob = t[1]

    #print device_class, ', ', highest_class
    if int(device_class) == int(highest_class):
        correct += 1

print 'Correct classes: ', 1.0*correct/50
'''
