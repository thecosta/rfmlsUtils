import os
import shutil
import pickle
import random
import numpy as np
import scipy.io as spio
from tqdm import tqdm

'''
Used to create the various pickle files for each device class' dataset. 

'''



def read_file_mat(file, keep_shape):
    '''
    Read data saved in .mat file
    Input: file path
    Output:
        -ex_data: complex signals
        -samples_in_example: example length
    '''
    mat_data = spio.loadmat(file)
    if mat_data.has_key('complexSignal'):
        complex_data = mat_data['complexSignal']  # try to use views here also
    elif mat_data.has_key('f_sig'):
        complex_data = mat_data['f_sig']
    if not keep_shape:
        real_data = np.reshape(complex_data.real, (complex_data.shape[1], 1))
        imag_data = np.reshape(complex_data.imag, (complex_data.shape[1], 1))
        complex_data = np.concatenate((real_data,imag_data), axis=1)
    samples_in_example =  complex_data.shape[0]
    return complex_data, samples_in_example


def read_file_pkl(file, keep_shape):
    '''
    Read data saved in .pkl file
    Input: file path
    Output:
        -ex_data: complex signals
        -samples_in_example: example length
    '''
    pickle_data = pickle.load(open(file, 'rb'))
    key_len = len(pickle_data.keys())
    if key_len == 1:
        complex_data = pickle_data[pickle_data.keys()[0]]
    elif key_len == 0:
        return None, 0
    else:
        raise Exception("{} {} Key length not equal to 1!".format(file, str(pickle_data.keys())))
        pass

    if complex_data.shape[0] == 0:
        return None, 0
    if not keep_shape:
        real_data = np.expand_dims(complex_data.real, axis=1)
        imag_data = np.expand_dims(complex_data.imag, axis=1)
        complex_data = np.concatenate((real_data,imag_data), axis=1)
    samples_in_example =  complex_data.shape[0]
    return complex_data, samples_in_example


def read_file(file, keep_shape):
    _, file_extension = os.path.splitext(file)  
    if 'mat' in file_extension:
        return read_file_mat(file, keep_shape)
    if 'pkl' in file_extension:
        return read_file_pkl(file, keep_shape)


def create_save_stats(label_path):
    """
    Compute Stats on the dataset
        The expected input is the path of the root folder for the dataset (folder containing n folders, one for each dataset), each folder should contain the label and partition pickle files. You can also provide as input the output folder.
        The output is a series of dictionaries and lists saved in pickle format in the output folder, in the same folder hierarchy as the input path.
        For each dataset, the following files are created:
    - stats : dictionary containing some general stats on the dataset 
    ['total_samples','avg_samples', 'total_examples', 'train_examples', 'test_examples', 'val_examples', 'avg_examples_per_device']
    """
    labels = pickle.load(open(os.path.join(label_path, 'label.pkl'), 'rb'))
    device_ids = pickle.load(open(os.path.join(label_path,'device_ids.pkl'), 'rb'))
    partition = pickle.load(open(os.path.join(label_path,'partition.pkl'), 'rb'))
    num_classes = len(device_ids.keys())

    all_examples = partition['train']
    if len(all_examples) is 0:
        print("This folder does not contain this type of data (it contains an empty partition file)")
        sys.exit(1)
        
    ex_per_device = {}
    for device in device_ids:
        ex_per_device[device] = 0  # init dictionary with zeros

    samples_per_example = {}
    total_samples = 0
    val_sum = np.zeros((2,))
    ex_cache = []
    skipped = 0

    for ex in tqdm(all_examples):
        ex_data, samples_in_example = read_file(ex,keep_shape=False)

        if ex_data is None or samples_in_example is 0:
            skipped = skipped + 1
            continue

        ex_per_device[labels[ex]] = ex_per_device[labels[ex]] + 1
        ex_cache.append(ex_data)
        val_sum = val_sum + ex_data.sum(axis=0)
        total_samples = total_samples + samples_in_example

    mean_val = val_sum / total_samples
    std_sum = np.zeros((2,))
    for ex in ex_cache:
        std_sum = std_sum + np.sum((ex-mean_val)**2, axis=0)
    std_val = np.sqrt(std_sum / total_samples)
    stats = {
        'total_samples': total_samples,
        'avg_samples': int(float(total_samples)/float(len(all_examples) - skipped)),
        'total_examples': len(all_examples),
        'skipped': skipped,
        'avg_examples_per_device': (len(all_examples) - skipped)/num_classes,
        'mean': mean_val,
        'std': std_val
    }
    with open(os.path.join(label_path,'stats.pkl'), 'wb') as handle:
        pickle.dump(stats, handle, protocol=pickle.HIGHEST_PROTOCOL)


path = '/scratch/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/'
dest_root = '/scratch/bruno/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/'
train_tsv = '/scratch/RFMLS/RFML_Test_Specs_Delivered_v3/test1/1Cv2.train.tsv'
test_tsv = '/scratch/RFMLS/RFML_Test_Specs_Delivered_v3/test1/1Cv2.test.tsv' 
train_examples = []
test_examples = []

with open(train_tsv, 'r') as f:
    for line in f:
        line = line[:-2]
        if 'W' not in line:
            continue
        train_examples.append(line)

with open(test_tsv, 'r') as f:
    for line in f:
        line = line[:-2]
        if 'W' not in line:
            continue
        test_examples.append(line)

#print test_examples

'''
    Format of device_ids.pkl.
    {
         ...
         'crane-gfi_1_dataset-9075': 12,
         'crane-gfi_1_dataset-9309': 14,
         ...
    }
'''
device_ids = path + 'device_ids.pkl'


'''
    Format of label.pkl.
    {
        ...
        u'/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/422/wifi_422_crane-gfi_1_dataset-7335/filtered_sig/WB-2988-3280_filtered.mat': 'crane-gfi_1_dataset-7335',
        u'/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/248/wifi_248_crane-gfi_1_dataset-7763/filtered_sig/WB-1814-2386_filtered.mat': 'crane-gfi_1_dataset-7763',
        ...
    }
'''
label = path + 'label.pkl'


'''
    Format of partition.pkl.
    {
        'train': [
                    ...
                    u'/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/2228/wifi_2228_crane-gfi_1_dataset-9404/filtered_sig/WB-1955-3992_filtered.mat',
                    u'/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/248/wifi_248_crane-gfi_1_dataset-7763/filtered_sig/WB-2224-1214_filtered.mat'
                    ... 
                 ]
    }
'''
partition = path + 'partition.pkl'


for i in tqdm(range(50)):
    new_device_ids = {}
    new_label = {}
    new_partition = {}

    dest = dest_root + str(i) + '/'
    dest_device_ids = dest + 'device_ids.pkl'
    dest_label = dest + 'label.pkl'
    dest_partition = dest + 'partition.pkl'

    if not os.path.exists(dest):
        os.makedirs(dest)

    with open(device_ids, 'r') as f:
        pkl = pickle.load(f)
        for key in pkl:
            if pkl[key] == i:
                device_id = key
            new_device_ids[key] = pkl[key]

    with open(label, 'r') as f:
        pkl = pickle.load(f)
        for key in pkl:
            if pkl[key] == device_id:
                new_label[key] = pkl[key]

    examples = new_label.keys()

    train_ex = []
    test_ex = []
    
    for example in examples:
        ex = example.split('/')[-1].split('.')[0].split('_')[0]
        #print example 
        if ex in train_examples:
            #print 'train'
            train_ex.append(example)
        if ex in test_examples:
            #print 'test'
            test_ex.append(example)

    #random.shuffle(examples)
    #l = len(examples)
    #split = int(l * 0.8)
    #train_ex = examples[:split]
    #test_ex = examples[-(l-split):]

    new_partition = {'train': train_ex, 'test': test_ex}

    with open(dest_device_ids, 'w') as f:
        pickle.dump(new_device_ids, f)

    with open(dest_label, 'w') as f:
        pickle.dump(new_label, f)

    with open(dest_partition, 'w') as f:
        pickle.dump(new_partition, f) 

    #create_save_stats(dest)
    #shutil.copy(path+'stats.pkl', dest+'stats.pkl')
