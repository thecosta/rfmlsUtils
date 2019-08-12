import glob
import pickle

order = [24, 41, 45, 29, 9, 18, 28, 43, 13, 3, 0, 4, 25, 20, 42, 37, 44, 38, 39, 35, 23, 7, 11, 31, 1, 49, 46, 32, 21, 30, 2, 6, 47, 14, 10, 48, 33, 8, 12, 16, 40, 36, 19, 15, 5, 34, 26, 22, 17, 27]
acc = [0.9818181818181818, 0.9454545454545454, 0.9090909090909091, 0.8909090909090909, 0.8545454545454545, 0.7818181818181819, 0.7636363636363637, 0.7454545454545455, 0.7090909090909091, 0.7090909090909091, 0.7090909090909091, 0.6909090909090909, 0.6727272727272727, 0.6727272727272727, 0.6545454545454545, 0.6545454545454545, 0.6363636363636364, 0.6363636363636364, 0.6181818181818182, 0.6, 0.6, 0.6, 0.5818181818181818, 0.5636363636363636, 0.5636363636363636, 0.5454545454545454, 0.5454545454545454, 0.5272727272727272, 0.5272727272727272, 0.509090909090909, 0.509090909090909, 0.4909090909090909, 0.4727272727272727, 0.4727272727272727, 0.4727272727272727, 0.45454545454545453, 0.45454545454545453, 0.45454545454545453, 0.43636363636363634, 0.41818181818181815, 0.4, 0.38181818181818183, 0.36363636363636365, 0.34545454545454546, 0.34545454545454546, 0.32727272727272727, 0.32727272727272727, 0.3090909090909091, 0.2727272727272727, 0.10909090909090909]
acc = []
files = glob.glob('/home/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit2/*/1C_raw_wifi/preds.pkl')

for i, device in enumerate(order):
    
    for log in files:

        if int(log.split('/')[-3]) == device: 
            result = False
            with open(log, 'r') as f:
                preds = pickle.load(f)
                device_acc = 0
                for device in preds['preds_exp']:
                    device_acc += preds['preds_exp'][device]

                acc.append(device_acc*1.0/55)
    '''
                for line in f:
                    line = line[:-1]
                    if line == '*************** Testing Model ***************':
                        result = True
                        continue
                    if result:
                        ex_acc = float(line.split(', ')[-1].split(')')[0])
                        #acc[i] = (acc[i], ex_acc)
                        acc.append(ex_acc)
                        result = False
    '''
print acc