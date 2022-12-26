import os

import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from cut import *
from z_mean import *
from coord3d_to_array import *
from draw import *
from conv2d import *


if __name__ == '__main__':
    root_path = r'/Users/dylan/Desktop/temp/magang/data/上表面/pcd'
    # for item in os.listdir(root_path):
    item = os.listdir(root_path)[0]
    file_id = os.path.splitext(item)[0]
    pcd_path = os.path.join(root_path, item)
    print(pcd_path)
    pcd = o3d.io.read_point_cloud(pcd_path)
    points = np.asarray(pcd.points)

    # floor, tail = cut1(points,file_id)
    # z_mean = z_mean1(points, floor, tail)
    # print(z_mean)

    array = coord3d_to_array(points)
    x_up, x_down, y_up, y_down = drop_nan(array)
    z_max, z_min = np.nanmax(array[x_up:x_down, y_up:y_down]), np.nanmin(array[x_up:x_down, y_up:y_down])
    array = fill_nan(array)  # need to fill nan
    array = array[x_up:x_down, y_up:y_down]
    img = draw_array2d(array, z_max, z_min)
    img.show()
    array_conv2d = conv2d(array, size=10)
    draw_array2d_new(array_conv2d,img0=img)
    pass
