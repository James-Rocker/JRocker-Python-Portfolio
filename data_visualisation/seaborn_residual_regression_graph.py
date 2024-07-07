# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:27:24 2018

@author: james
"""

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from Seaborn:
tips = sns.load_dataset("tips")

# Create a residual plot
sns.residplot(data=tips, x="total_bill", y="tip")

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/residplot.png")
