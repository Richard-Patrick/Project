# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:41:25 2022

@author: Richard Patrick
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 


# Creating equally spaced 100 data in range 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Generating x and y data
x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)



# Plotting
plt.plot(x, y)
plt.title('Heart Shape')
plt.show()
    

def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x

# prepare some coordinates
n = 40
xr = np.linspace(-1.3,1.3,n)
yr = np.linspace(-1.3,1.3,n)
zr = np.linspace(-1.3,1.3,n)
xr, yr, zr = np.meshgrid(xr, yr, zr)
x = midpoints(xr)
y = midpoints(yr)
z = midpoints(zr)

# define a heart
heart = (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3 < 0

#plot
fig = plt.figure(figsize=(6,6))
ax = fig.gca(projection='3d')
ax.voxels(xr, yr, zr, heart, facecolor="r",edgecolors='w',linewidth=0.2)
#ax.set_aspect('equal')
plt.savefig("3Dvoxel_heart.png", dpi=100,transparent = False)
plt.show()



    


















    