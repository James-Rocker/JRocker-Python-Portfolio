# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:08:57 2018

@author: james
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# TODO: fix the file import
filename = ""
df = pd.read_csv(filename)

# Create box plot with Seaborn's default settings
sns.boxplot(x="", y="", data=df)

# Label the axes
plt.xlabel("")
plt.ylabel("")

# Show the plot
plt.show()
