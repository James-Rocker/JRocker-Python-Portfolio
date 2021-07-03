# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 06:42:35 2018

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator and initialize
np.random.seed(42)
random_numbers = np.empty(100000)

# Generate random numbers
for i in range(100000):
    random_numbers[i] = np.random.random()

plt.hist(random_numbers)
plt.show()
