# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 07:26:41 2018

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt
from ecdf import ecdf

samples_std1 = np.random.normal(20, 1, 100000)
samples_std3 = np.random.normal(20, 3, 100000)
samples_std10 = np.random.normal(20, 10, 100000)

# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
plt.plot(x_std1, y_std1, marker='.', linestyle = 'none')
plt.plot(x_std3, y_std3, marker='.', linestyle = 'none')
plt.plot(x_std10, y_std10, marker='.', linestyle = 'none')

# Make 2% margin
plt.margins(0.40)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()