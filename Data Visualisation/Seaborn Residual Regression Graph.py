# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:27:24 2018

@author: james
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("")

# Generate a red residual plot for visualizing how far datapoints diverge from the regression line
sns.residplot(x=df[0], y=df[1], data=df, color="red")

# Display the plot
plt.show()
