# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:16:28 2018

I had no idea seaborn had a penguin dataset built in!

@author: james
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from Seaborn:
penguins = sns.load_dataset("penguins")

# Create a lmplot of penguins bill length to bill depth by species
sns.lmplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/linear_plot.png")
