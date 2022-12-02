import numpy as np
import matplotlib.pyplot as plt


def cut1(points):
    z = points[:, 2]
    z_max, z_min = np.max(z), np.min(z)
    z_count = z.shape[0]

    bins = int((z_max - z_min))
    mask = (z_count / bins) * 1
    hist = np.histogram(z, bins)[0]
    bool_hist = (hist > mask).astype(int)
    bool_hist[0], bool_hist[-1] = 0, 0
    flip_hist = bool_hist[1:] - bool_hist[:-1]
    start_mask = np.where(flip_hist == 1)[0]
    end_mask = np.where(flip_hist == -1)[0]
    size = (z_max - z_min) / bins
    start = start_mask * size + z_min
    end = end_mask * size + z_min
    print(start)
    print(end)

    assert start.shape[0] == end.shape[0]
    max_particles = 0
    max_index = -1
    for i in range(start.shape[0]):
        if start[i] < 5 or end[i] > -5:
            continue
        count = np.sum(hist[start_mask[i]: end_mask[i]])
        if count > max_particles:
            max_particles = count
            max_index = i
    floor, tail = start[max_index], end[max_index]

    return floor, tail

    # z_sorted = np.sort(z)
    #
    # z_part1 = z_sorted[z_sorted < floor]
    # count1 = z_part1.shape[0]
    # plt.plot(range(count1), z_part1, 'b')
    #
    # z_part2 = z_sorted[np.logical_and(z_sorted > floor, z_sorted < tail)]
    # count2 = count1 + z_part2.shape[0]
    # plt.plot(range(count1, count2), z_part2, 'r')
    #
    # z_part3 = z_sorted[z_sorted > tail]
    # count3 = count2 + z_part3.shape[0]
    # plt.plot(range(count2, count3), z_part3, 'b')
    #
    # # if max_index != -1:
    #
    # plt.grid()
    # plt.show()
    # size = 1.00
    # bins = int((z_max-z_min)/size)
    # hist = np.histogram(z, bins)[0]

    # plt.hist(z,bins=1024)
    # plt.show()
