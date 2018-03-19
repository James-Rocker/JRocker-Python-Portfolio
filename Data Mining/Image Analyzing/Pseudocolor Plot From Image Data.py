# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:49:05 2018

@author: james
"""
import matplotlib.pyplot as plt

# Load the image into an array: img
img = plt.imread('900px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()
