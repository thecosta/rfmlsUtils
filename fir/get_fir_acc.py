import glob
import pickle
import numpy as np


def get_epoch_time(logs):
    tot_time = 0.0
    tot_slice_acc = 0.0
    avg_epochs = 0
    for log in logs:
        log_file = []
        with open(log, 'r') as f:
            for line in f:
                line = line[:-1]
                log_file.append(line)

        epochs = log_file[-4]
        epochs = epochs.split(':')[0] 
        if 'resnet' in log:
            print epochs

        try:
            epochs = int(epochs[5:])
        except:
            continue
        avg_epochs += epochs

        time = log_file[-6]
        if time == '':
            time = log_file[-7]

        try:
            time = time.split('-')[1]
        except:
            continue
        time = time.split('s')[0]
        try:
            tot_time += int(time)*epochs
        except:
            continue
        acc = log_file[-1]
        acc = acc[1:]
        slice_acc = acc.split(',')[0]
        tot_slice_acc += float(slice_acc)

    #avg_time = tot_time / len(logs)        
    avg_epochs = avg_epochs / len(logs)
    avg_slice_acc = tot_slice_acc / len(logs)
    tot_time = tot_time / (60 * 60)    

    return tot_time, avg_slice_acc, avg_epochs

def get_predictions(predictions):
    '''
    Get prediction accuracies from a list of preds.pkl files.
    input:
        - predictions: list of preds.pkl file locations
    '''    

    results = []
    for preds in predictions:

        device = int(preds.split('/')[-3])
        tot_ex = 0 
        corr = 0

        with open(preds, 'r') as f:
            preds_pkl = pickle.load(f)

            for pred in preds_pkl['preds_exp']:
                pred = preds_pkl['preds_exp'][pred]
                tot_ex += 1
                if np.argmax(pred) == device:
                    corr += 1
                
        results.append((device, 1.0*corr/tot_ex))

    return results


def get_ordered_predictions(device_order, predictions):
    '''
    Get predictions and accuracies from predictions in a given device order.
    input:
        - device_order: list of numbers representing device classes
        - predictions: list of preds.pkl file locations
    '''
    results, acc = [], []
    for order in device_order:
        for preds in predictions:

            device = int(preds.split('/')[-3])
            tot_ex = 0
            corr = 0

            if int(device) != order:
                continue

            with open(preds, 'r') as f:
                preds_pkl = pickle.load(f)
                device_acc = 0
                for pred in preds_pkl['preds_exp']:
                    pred = preds_pkl['preds_exp'][pred]

                    tot_ex += 1
                    if np.argmax(pred) == device:
                        corr += 1

            results.append((device, 1.0*corr/tot_ex))
            acc.append(corr*1.0/tot_ex) 

    return results, acc



if __name__ == '__main__':

    taps_5 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_5taps_probsum/*/1C_raw_wifi/preds.pkl')
    taps_11 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_11taps_xavier/*/1C_raw_wifi/preds.pkl')
    taps_15 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_15taps_xavier/*/1C_raw_wifi/preds.pkl')
    taps_20 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_20taps_xavier/*/1C_raw_wifi/preds.pkl')
    taps_30 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_30taps_xavier/*/1C_raw_wifi/preds.pkl')    
    taps_100 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_100taps_xavier/*/1C_raw_wifi/preds.pkl')
    taps_eq_100 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/equalized/baseline/firinit_100taps_xavierk16/*/1C_equalized_wifi/preds.pkl')
    taps_11_res = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/resnet1d/firinit_11taps_xavierk16/*/1C_raw_wifi/preds.pkl')

    #taps_15.sort()
    #taps_20.sort()
    #taps_15 = taps_15[:20]
    #taps_20 = taps_20[:20]    

    log_5 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_5taps_probsum/*/log.out')
    log_11 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_11taps_xavier/*/log.out')
    log_15 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_15taps_xavier/*/log.out')
    log_20 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_20taps_xavier/*/log.out')
    log_30 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_30taps_xavier/*/log.out')
    log_100 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/baseline/firinit_100taps_xavier/*/log.out')
    log_eq_100 = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/equalized/baseline/firinit_100taps_xavierk16/*/log.out')
    log_11_res = glob.glob('/scratch/bruno/RFMLS/results/fir/1C/wifi/raw/resnet1d/firinit_11taps_xavierk16/*/log.out')

    
    time_5, slice_acc_5, epoch_5 = get_epoch_time(log_5)
    time_11, slice_acc_11, epoch_11 = get_epoch_time(log_11)
    time_15, slice_acc_15, epoch_15 = get_epoch_time(log_15)
    time_20, slice_acc_20, epoch_20 = get_epoch_time(log_20)
    time_30, slice_acc_30, epoch_30 = get_epoch_time(log_30)
    time_100, slice_acc_100, epoch_100 = get_epoch_time(log_100)
    time_eq_100, slice_eq_acc_100, epoch_eq_100 = get_epoch_time(log_eq_100)
    time_11_res, slice_acc_11_res, epoch_11_res = get_epoch_time(log_11_res)    

    results_5 = get_predictions(taps_5)

    results_5 = np.array(results_5, dtype=[('device', int), ('acc', float)])
    results_5 = np.flip(np.sort(results_5, order='acc'))

    acc_5 = []
    device_order = []
    device_order_str = []
    for t in results_5:
        acc_5.append(t[1])
        device_order.append(t[0])
        device_order_str.append(str(t[0]))
    
    results_11, acc_11 = get_ordered_predictions(device_order, taps_11)
    results_15, acc_15 = get_ordered_predictions(device_order, taps_15)
    results_20, acc_20 = get_ordered_predictions(device_order, taps_20)
    results_30, acc_30 = get_ordered_predictions(device_order, taps_30)
    results_100, acc_100 = get_ordered_predictions(device_order, taps_100)
    results_eq_100, acc_eq_100 = get_ordered_predictions(device_order, taps_eq_100)
    results_11_res, acc_11_res = get_ordered_predictions(device_order, taps_11_res)

    print '5 taps: (', slice_acc_5, ', ', np.mean(acc_5), ')'
    print '5 taps: ', epoch_5, ', time: ', time_5, ' hours\n'

    print '11 taps: (', slice_acc_11, ', ', np.mean(acc_11), ')'
    print '11 taps: ', epoch_11, ', time: ', time_11, ' hours\n'

    print '15 taps: (', slice_acc_15, ', ', np.mean(acc_15), ')'
    print '15 taps: ', epoch_15, ', time: ', time_15, 'hours\n'

    print '20 taps: (', slice_acc_20, ', ', np.mean(acc_20), ')'
    print '20 taps: ', epoch_20, ', time: ', time_20, ' hours\n'

    print '30 taps: (', slice_acc_30, ', ', np.mean(acc_30), ')'
    print '30 taps: ', epoch_30, ', time: ', time_30, ' hours\n'

    print '100 taps: (', slice_acc_100, ', ', np.mean(acc_100), ')'
    print '100 taps: ', epoch_100, ', time: ', time_100, ' hours\n'

    print '100 taps eq: (', slice_eq_acc_100, ', ', np.mean(acc_eq_100), ')'
    print '100 taps eq: ', epoch_eq_100, ', time: ', time_eq_100, ' hours\n'

    print '11 taps resnet: (', slice_acc_11_res, ', ', np.mean(acc_11_res), ')'
    print '11 taps resnet, epochs: ', epoch_11_res, ', time: ', time_11_res, ' hours\n'
