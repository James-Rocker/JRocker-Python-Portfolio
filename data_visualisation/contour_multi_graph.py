# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:14:53 2018

@author: james
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate two 1-D arrays: u, v
# Linspace is between the first 2 values and returns the even spaced third number of samples
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 20)

# Generate 2-D arrays from u and v: X, Y
X, Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3 * np.sqrt(X**2 + Y**2))

# Generate a default contour map of the array Z
plt.subplot(2, 2, 1)
plt.contour(X, Y, Z, cmap="autumn")
plt.colorbar()
plt.title("Autumn")

# Generate a contour map with 20 contours
plt.subplot(2, 2, 2)
plt.contour(X, Y, Z, 20, cmap="summer")
plt.colorbar()
plt.title("Summer")

# Generate a default filled contour map of the array Z
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z, cmap="winter")
plt.colorbar()
plt.title("Winter")

# Generate a default filled contour map with 20 contours
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z, 20, cmap="spring")
plt.colorbar()
plt.title("Spring")

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()
