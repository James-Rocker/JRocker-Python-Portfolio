# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 07:26:41 2018
Used to generate the cumulative distribution function

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt
from empirical_distribution_function import empirical_dist

"""
Let's try and see the difference of scale numpy makes when building a random size array

Creates 3 numpy arrays with a mean (centre) of 20 and a variety of standard deviation scale
with a sample size of 100000 and variety of scales
"""
samples_std1 = np.random.normal(20, 1, 100000)
samples_std3 = np.random.normal(20, 3, 100000)
samples_std10 = np.random.normal(20, 10, 100000)

# Generate the
x_std1, y_std1 = empirical_dist(samples_std1)
x_std3, y_std3 = empirical_dist(samples_std3)
x_std10, y_std10 = empirical_dist(samples_std10)

# Let's plot these values
plt.plot(x_std1, y_std1, marker=".", linestyle="none")
plt.plot(x_std3, y_std3, marker=".", linestyle="none")
plt.plot(x_std10, y_std10, marker=".", linestyle="none")

# Small 2% margin
plt.margins(0.02)

# Make a legend and show the plot
plt.legend(("std = 1", "std = 3", "std = 10"), loc="lower right")
plt.show()
