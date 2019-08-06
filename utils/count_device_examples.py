import glob
import pickle
import numpy

path = '/scratch/bruno/RFMLS/dec18_darpa/v3_list/raw_samples/1Cv2/wifi/*'

folders = glob.glob(path)

data = []

for folder in folders:
    device = folder.split('/')[-1]
    partition = folder + '/partition.pkl'
    with open(partition, 'r') as f:
        pkl = pickle.load(f)
    train_set = pkl['train']
    test_set = pkl['test']
    data.append((device, len(train_set), len(test_set)))

print(data[:100])
