import glob
import pickle
import numpy as np


baseline = glob.glob('/home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_10taps/*/1C_raw_wifi/preds.pkl')
taps_5 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_5taps_probsum/*/1C_raw_wifi/preds.pkl')
taps_11 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_11taps_probsum/*/1C_raw_wifi/preds.pkl')

results_5, results_10, results_11 = [], [], [] 
acc_5, acc_10, acc_11 = [], [], []

for preds in taps_5:

    tot_prob = np.zeros(shape=(50,))
    device = int(preds.split('/')[-3])
    tot_ex = 0 
    acc = 0

    with open(preds, 'r') as f:
        preds_pkl = pickle.load(f)

        for pred in preds_pkl['preds_exp']:
            pred = preds_pkl['preds_exp'][pred]

            tot_ex += 1
            if np.argmax(pred) == device:
                acc += 1
            
    results_5.append((device, 1.0*acc/tot_ex))


results_5 = np.array(results_5, dtype=[('device', int), ('acc', float)])
results_5 = np.flip(np.sort(results_5, order='acc'))


device_order = []
device_order_str = []
for t in results_5:
    acc_5.append(t[1])
    device_order.append(t[0])
    device_order_str.append(str(t[0]))


for order in device_order:
    for preds in taps_11:

        tot_prob = np.zeros(shape=(50,))
        device = int(preds.split('/')[-3])
        tot_ex = 0
        acc = 0

        if int(device) != order:
            continue

        with open(preds, 'r') as f:
            preds_pkl = pickle.load(f)
            device_acc = 0
            for pred in preds_pkl['preds_exp']:
                pred = preds_pkl['preds_exp'][pred]

                tot_ex += 1
                if np.argmax(pred) == device:
                    acc += 1

        results_11.append((device, 1.0*acc/tot_ex))
        acc_11.append(acc*1.0/tot_ex) 

'''
for order in device_order:
    for preds in taps_11:

        device = preds.split('/')[-3]

        if int(device) != order:
            continue

        with open(preds, 'r') as f:
            preds_pkl = pickle.load(f)
            device_acc = 0
            for pred in preds_pkl['preds_exp']:
                device_acc += preds_pkl['preds_exp'][pred]
            
            acc = device_acc*1.0/len(preds_pkl['preds_exp'])
            acc_11.append(acc)
            results_11.append((device, acc))
'''

#print device_order_str
#print device_order
print(acc_11)
#print np.mean(acc_5)
#print(np.mean(acc_11))
#print(device_order)
