import matplotlib.pyplot as plt
import numpy as np


def z_mean1(points, floor, tail):
    points = points[np.logical_and(points[:, 2] > floor + 2, points[:, 2] < tail - 2)]
    z = points[:, 2]
    z = np.sort(z)
    z_count = z.shape[0]
    bins = int(z_count / 10000)
    plt.hist(z, bins)
    z_max, z_min = np.max(z), np.min(z)
    size = (z_max - z_min)/bins
    print(size)

    z_mark = None
    z_last = None
    count = 0
    ceil = 0
    value = None
    for i in range(z_count):
        if i == 0:
            z_last = z[i]
            count = 1
        if z_last == z[i]:
            count += 1
        else:
            if z_mark is not None:
                width = z_last - z_mark
                height = count/width
                if height > ceil:
                    ceil = height
                    value = (z_mark+z_last)/2
                    print(width)
            z_mark = z_last
            z_last = z[i]
            count = 1

    plt.plot([value],[ceil/33],'r.')

    plt.show()
    return value