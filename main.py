import os

import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from cut import *
from z_mean import *
from coord3d_to_array import *

if __name__ == '__main__':
    root_path = r'/Users/dylan/Desktop/temp/magang/data/上表面/pcd'
    for item in os.listdir(root_path):
        file_id = os.path.splitext(item)[0]
        pcd_path = os.path.join(root_path,item)
        print(pcd_path)
        pcd = o3d.io.read_point_cloud(pcd_path)
        points = np.asarray(pcd.points)


        # floor, tail = cut1(points,file_id)
        # z_mean = z_mean1(points, floor, tail)
        # print(z_mean)

        array = coord3d_to_array(points)
        array_fillna = fill_nan(array)  # need to fill nan




