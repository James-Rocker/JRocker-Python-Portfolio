# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:06:47 2018

@author: james
"""
import matplotlib.pyplot as plt

# Load the image into an array: image
image = plt.imread('900px-Astronaut-EVA.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256), normed=True, color='red', alpha=0.4)

# Display the plot
plt.show()
