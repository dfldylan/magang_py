# import tensorflow as tf
import numpy as np
from scipy import signal

def conv2d(array, size):
    kernel = np.ones(shape=[3*size,3*size])
    kernel[size:2*size,size:2*size] *= -8
    ret = signal.convolve2d(array, kernel,mode='valid')
    return ret
