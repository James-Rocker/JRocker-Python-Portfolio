# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:19:44 2018

@author: james
"""
import matplotlib.pyplot as plt

# Load the image into an array: img
img = plt.imread('900px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image pixel columns, rows then colour chanels 
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()
