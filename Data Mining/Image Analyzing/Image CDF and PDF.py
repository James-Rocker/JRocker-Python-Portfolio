# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:17:24 2018

@author: james
"""

import matplotlib.pyplot as plt
 # Probability Distribution Function (PDF).
 # Cumulative Distribution Function (CDF)

image = plt.imread('900px-Astronaut-EVA.jpg')
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0,256), normed=True, cumulative=True,
               color='blue', alpha=0.4)
               
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF - red & CDF - blue (original image)')
plt.show()

