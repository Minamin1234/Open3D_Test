import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import sys

ply = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply.path)
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd],
zoom=0.3412,
front=[0.4257, -0.2125, -0.8795],
lookat=[2.6172, 2.0475, 1.532],
up=[-0.0694, -0.9768, 0.2024])