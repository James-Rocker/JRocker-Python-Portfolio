# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:20:33 2018

@author: james
"""

import matplotlib.pyplot as plt
import numpy as np

u = np.linspace(-50, 50)
v = np.linspace(-100, 100)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

# Generate a 2-D histogram based on 1d
plt.hist2d(u, v, bins=(50, 50),range=((-100, 100), (-100, 100)))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('X axis values')
plt.ylabel('Y axis values')
plt.title('hist2d() plot')
plt.show()
