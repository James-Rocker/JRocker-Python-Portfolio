# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 06:45:12 2018

@author: James
"""

import numpy as np
import matplotlib.pyplot as plt

# Show the difference in distribution accross different std
samples_std1 = np.random.normal(20, 1, 100000)
samples_std3 = np.random.normal(20, 3, 100000)
samples_std10 = np.random.normal(20, 10, 100000)

# Make histograms
plt.hist(samples_std1, normed=True, histtype='step', bins=100)
plt.hist(samples_std3, normed=True, histtype='step', bins=100)
plt.hist(samples_std10, normed=True, histtype='step', bins=100)
plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.title('Visualising std Differences')
plt.show()
