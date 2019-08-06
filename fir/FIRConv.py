import numpy as np
import tensorflow as tf
import scipy.io as spio
from keras import backend as K

def read_file_mat(file):
    # Real hard work here
    mat_data = spio.loadmat(file)
    if mat_data.has_key('complexSignal'):
        complex_data = mat_data['complexSignal']  # try to use views here also
    elif mat_data.has_key('f_sig'):
        complex_data = mat_data['f_sig']
    real_data = np.reshape(complex_data.real, (complex_data.shape[1], 1))
    imag_data = np.reshape(complex_data.imag, (complex_data.shape[1], 1))
    samples_in_example =  real_data.shape[0]
    ex_data = np.concatenate((real_data,imag_data), axis=1)
    return ex_data, samples_in_example


def FIRConv(X, kernel, verbose=0):
    '''
        Input:
            - X: signal with shape (N, 2)
            - kernel: filter to convolve X with, shape (M, 2)
        Output:
            - Filtered signal
    '''
    slice_size = len(X)
    
    X_real = X[:, 0] # (N, 1)
    X_img = X[:, 1] # (N, 1)

    kernel_real = kernel[:, 0] # (M, )
    kernel_img = kernel[:, 1] # (M, )
    
    real = np.convolve(X_real, kernel_real) - np.convolve(X_img, kernel_img)
    img = np.convolve(X_real, kernel_img) + np.convolve(X_img, kernel_real)

    real = real[:slice_size]
    img = img[:slice_size]    
    
    X_filtered = np.transpose(np.stack([real, img]))


    if verbose: 
        print 'input shape: ', X.shape
        print 'X: ', X.shape # (N, 2)
        print 'kernel: ', kernel.shape
        print 'X_real: ', X_real.shape
        print 'X_img: ', X_img.shape
        print 'kernel_real: ', kernel_real.shape
        print 'kernel_img: ', kernel_img.shape
        print 'real: ', real.shape
        print 'img: ', img.shape
        print 'output shape: ', X_filtered.shape
        print 'L2 distance: ', np.linalg.norm(X_filtered-X, ord=2)

    
    return X_filtered


if __name__ == '__main__':
    path = '/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/11/wifi_11_crane-gfi_1_dataset-10550/filtered_sig/WB-1041-1161_filtered.mat'
    path2 = '/scratch/RFMLS/dec18_darpa/v3/1Cv2/wifi/1592/wifi_1592_crane-gfi_1_dataset-1841/filtered_sig/WB-125-2197_filtered.mat'

    #ex_data, samples_in_example = read_file_mat(path)
    X = np.random.normal(size=(1000,2))
    FIRConv(X)
