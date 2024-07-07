# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:41:26 2018

@author: james
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# load the example dataset
tips = sns.load_dataset('tips')

# Create a scatter plot of total bill vs tip amount:
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips)

# Perform linear regression and add the regression line to the plot:
sns.regplot(x='total_bill', y='tip', data=tips, ci=None)

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/linear_regression_scatter_plot.png")
