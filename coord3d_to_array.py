import numpy as np
import multiprocessing.dummy as mp
import pandas as pd

def coord3d_to_array(points):
    x_unique = np.unique(points[:, 0])  # need to remove '0'
    y_unique = np.unique(points[:, 1])  # start from '0', always 4096 items?

    # x
    x_unique = x_unique[1:]
    x_min = x_unique[0]
    x_bn = x_unique - x_min
    x_unit = x_bn[-1] / (x_bn.shape[0] - 1)
    ## x_index = np.fix((x - x_min)/x_unit)

    # y
    y_unit = y_unique[-1] / (y_unique.shape[0] - 1)
    ## y_index = np.fix(y/y_unit)

    ret = np.nan * np.ones([x_unique.shape[0],y_unique.shape[0]])
    points_valid = points[points[:,0]!=0]
    coord_x = np.around((points_valid[:,0]-x_min)/x_unit)
    coord_y = np.around(points_valid[:,1]/y_unit)
    coord = np.vstack([coord_x,coord_y]).transpose().astype(int)
    z = points_valid[:, 2]

    def _fill_ret(inputs):
        _coord, a_point = inputs
        ret[_coord[0],_coord[1]] = a_point


    mp.Pool().map(_fill_ret, zip(coord, z))

    return ret
