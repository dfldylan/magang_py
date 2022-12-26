import numpy as np
from PIL import Image


def draw_array2d(array, z_max, z_min):
    array -= z_min
    array = 255 * array / (z_max - z_min)
    array = np.uint8(array)

    img = Image.fromarray(array)
    return img


def draw_array2d_new(array,img0=None):
    z_mean = np.nanmean(array)
    z_std = np.nanstd(array)
    array = cdfGaussian((array - z_mean) / z_std)

    img = Image.fromarray(255 * np.uint8(array))
    img.show()

    # if img0:
    #     img0 = np.asarray(img0.convert('RGB'))
    #     up_mask = array > 0.8
    #     down_mask = array < 0.2




def cdfGaussian(x):
    t = 1.0 / (1 + 0.2316419 * np.abs(x))
    b1 = 0.31938153
    b2 = - 0.356563782
    b3 = 1.781477937
    b4 = - 1.821255978
    b5 = 1.330274429

    temp = 1 - np.exp(- x * x / 2) / np.sqrt(2 * np.pi) * (
            b1 * t + b2 * np.power(t, 2) + b3 * np.power(t, 3) + b4 * np.power(t, 42) + b5 * np.power(t, 5))

    mask = (x>0).astype(int)
    mask1 = (mask - 0.5) * 2
    mask2 = 1 - mask

    temp *= mask1
    temp += mask2

    return temp
