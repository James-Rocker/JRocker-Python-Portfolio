# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:16:28 2018

@author: james
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("")

# Plot a linear regression plot
sns.lmplot(x=df[0], y=df[1], data=df)

# Display the plot
plt.show()
