import os
import pickle
import numpy as np

#base_path = '/scratch/bruno/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/6/'
base_path = '/scratch/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/'
with open(os.path.join(base_path, "partition.pkl"),'r') as f:
    partition = pickle.load(f)

test_list = partition['test']

preds_path = '/home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firbinary_all/1C_raw_wifi/preds.pkl'
with open(preds_path, 'rb') as f:
    preds = pickle.load(f)

with open(os.path.join(base_path, "device_ids.pkl"), 'r') as f:
    device_ids = pickle.load(f)

with open(os.path.join(base_path, "label.pkl"),'r') as f:
    labels = pickle.load(f)

classes = np.max([device_ids[labels[ex]] for ex in test_list])+1
preds_exp = preds['preds_exp']

dtype = [('device', int), ('exp', int), ('total', int)]

counts = np.zeros((classes), dtype=dtype)

for ex in test_list:
    real_label = device_ids[labels[ex]]
    counts[real_label][0] = real_label
    counts[real_label][2] += 1
    counts[real_label][1] += preds_exp[ex]

dtype = [('device', int), ('acc', float)]
acc_counts = np.zeros((classes), dtype=dtype)

for i, result in enumerate(counts):
    acc = counts[i][1]*1.0/counts[i][2]
    acc_counts[i][0] = counts[i][0]
    acc_counts[i][1] = acc

acc_counts = np.flip(np.sort(acc_counts, order='acc'))

for i, result in enumerate(acc_counts):
    #print acc_counts[i][0], ', ', acc_counts[i][1]
    print acc_counts[i][1]
#print acc_counts
