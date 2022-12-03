import numpy as np
import matplotlib.pyplot as plt


def cut1(points, name):
    z = points[:, 2]
    z_max, z_min = np.max(z), np.min(z)
    z_count = z.shape[0]

    bins = int((z_max - z_min))  # 区间数量
    mask = (z_count / bins) * 1  # 判定有效区间的粒子数阈值
    hist = np.histogram(z, bins)[0]  # 统计每个区间的粒子数
    bool_hist = (hist > mask).astype(int)  # 阈值掩膜，1为有效区间，0为无效区间
    bool_hist[0], bool_hist[-1] = 0, 0
    flip_hist = bool_hist[1:] - bool_hist[:-1]  # 1为上升沿，-1为下降沿
    start_mask = np.where(flip_hist == 1)[0]  # 上升沿idx，下面是下降沿idx
    end_mask = np.where(flip_hist == -1)[0]
    size = (z_max - z_min) / bins  # 每个区间的大小
    start = start_mask * size + z_min  # 每个区间开始的z值
    end = end_mask * size + z_min  # # 每个区间结束的z值
    print(start)
    print(end)

    # 下面是找粒子数最大的那个区间
    assert start.shape[0] == end.shape[0]
    max_particles = 0
    max_index = -1
    for i in range(start.shape[0]):
        # if start[i] < 0 and end[i] > 0:
        #     continue
        count = np.sum(hist[start_mask[i]:end_mask[i]])
        if count > max_particles:
            max_particles = count
            max_index = i
    floor, tail = start[max_index], end[max_index]

    # 下面是绘图，可注释掉
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
    # plt.grid()
    # # plt.savefig(os.path.join('save/cut', name))
    # plt.close()
    # # plt.show()

    return floor, tail
