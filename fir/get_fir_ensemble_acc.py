import os
import glob
import pickle
import numpy as np


device_paths = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_ensemble_11taps_probsum2/*')

example_acc = {}

firmodel_acc = []
firmodel_acc_ensemble = {}

device_acc = []
device_acc_ensemble = []

total_devices = 0
correct_devices = 0

# Iterate over device classes
for device_path in device_paths:

    fir_models = glob.glob(device_path + '/*/1C_raw_wifi/preds.pkl')    
    
    ## Edit
    #np.random.shuffle(fir_models)
    #fir_models = [fir_models[0]]
    ##

    total_device_prob = np.array([50,])
    total_device_examples = 0
    correct_device_examples = 0
    total_devices += 1
    
    # Iterate over all FIR models
    for fir_model in fir_models:

        device_n = int(fir_model.split('/')[-4])
        weight_n = int(fir_model.split('/')[-3])

        total_fir_prob = np.array([50,])
        total_fir_examples = 0
        correct_fir_examples = 0
    
        real_label = device_n

        with open(fir_model, 'r') as f:
            preds_pkl = pickle.load(f)

            # Iterate over all examples
            for pred in preds_pkl['preds_exp']:

                predictions = preds_pkl['preds_exp'][pred]
                total_fir_prob = total_fir_prob + predictions
                total_device_prob = total_device_prob + predictions

                total_fir_examples += 1
                total_device_examples += 1

                predicted_example = np.argmax(predictions)

                if device_n == predicted_example:
                    correct_fir_examples += 1
                    correct_device_examples += 1
        
        # FIR argmax of each example
        firmodel_acc.append((weight_n, correct_fir_examples, total_fir_examples))

        # FIR argmax of all prob vectors
        if np.argmax(total_fir_prob) == device_n:
            if device_n in firmodel_acc_ensemble:
                firmodel_acc_ensemble[device_n] += 1
            else:
                firmodel_acc_ensemble[device_n] = 1
        
        # End of FIR model loop
                                
    d_acc = 1.0*correct_device_examples / total_device_examples
    device_acc.append((device_n, d_acc))
    
    if np.argmax(total_device_prob) == device_n:
        device_acc_ensemble.append((device_n, 1.0))
    else:
        device_acc_ensemble.append((device_n, 0.0))


for key in firmodel_acc_ensemble:
    firmodel_acc_ensemble[key] = 1.0*firmodel_acc_ensemble[key]/50


# Get final results for firmodel_acc
tmp = []
for n in range(total_devices):
    correct = 0
    total = 0
    for t in firmodel_acc:
        if t[0] == n:
            correct += t[1]
            total += t[2]
    try:
        tmp.append((n, 1.0*correct/total))    
    except:
        tmp.append((n, 0))
firmodel_acc = tmp
firmodel_acc = np.array(firmodel_acc, dtype=[('device', int), ('acc', float)])
firmodel_acc = np.flip(np.sort(firmodel_acc, order='acc'))

# Get average for device_acc
firmodel_acc_avg = 0.0
for t in firmodel_acc:
    firmodel_acc_avg += t[1]
firmodel_acc_avg = firmodel_acc_avg * 1.0 / total_devices


# Get final results for firmodel_acc_ensemble
order = []
for t in firmodel_acc:
    order.append(t[0])

tmp = []
for n in order:
    for t in firmodel_acc_ensemble:
        if t == n:
            tmp.append((n, firmodel_acc_ensemble[t]))
firmodel_acc_ensemble = tmp

# Get average for firmodel_acc_ensemble
firmodel_acc_ensemble_avg = 0.0
for t in firmodel_acc_ensemble:
    firmodel_acc_ensemble_avg += t[1]
firmodel_acc_ensemble_avg = firmodel_acc_ensemble_avg * 1.0 / total_devices


# Get final results for device_acc
device_acc = np.array(device_acc, dtype=[('device', int), ('acc', float)])
device_acc = np.flip(np.sort(device_acc, order='acc'))
order = []
for t in device_acc:
    order.append(t[0])

# Get average for device_acc
device_acc_avg = 0.0
for t in device_acc:
    device_acc_avg += t[1]
device_acc_avg = device_acc_avg * 1.0 / total_devices


# Get final results for device_acc_ensemble
tmp = []
for n in order:
    for t in device_acc_ensemble:
        if t[0] == n:
            tmp.append(t)
device_acc_ensemble = tmp

# Get average for device_acc_ensemble
device_acc_ensemble_avg = 0.0
for t in device_acc_ensemble:
    device_acc_ensemble_avg += t[1]
device_acc_ensemble_avg = device_acc_ensemble_avg * 1.0 / total_devices


print 'FIR Argmax per example:\n',  firmodel_acc
print 'FIR Argmax per example avg: ', firmodel_acc_avg, '\n'

print 'FIR Argmax per dataset:\n', firmodel_acc_ensemble
print 'FIR Argmax per dataset avg: ', firmodel_acc_ensemble_avg, '\n'

print 'Device Argmax per example:\n', device_acc
print 'Device Argmax per example avg: ', device_acc_avg, '\n'

print 'Device Argmax per dataset:\n', device_acc_ensemble
print 'Device Argmax per dataset avg: ', device_acc_ensemble_avg, '\n'
