# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:08:53 2018

@author: James
"""

import matplotlib.pyplot as plt
import seaborn as sns


# Load the tips dataset from Seaborn
tips = sns.load_dataset("tips")

# Create a pair plot with scatterplot, histogram on each axis, and regression line
sns.pairplot(data=tips, kind="hist")

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/pair_plot.png")
