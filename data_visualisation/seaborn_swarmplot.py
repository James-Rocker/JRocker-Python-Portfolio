# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:34:36 2018

@author: James
"""
import matplotlib.pyplot as plt
import seaborn as sns

# Load the penguins dataset from Seaborn:
penguins = sns.load_dataset('penguins')

# Create a swarm plot of flipper length vs species
sns.swarmplot(x="flipper_length_mm", y="species", data=penguins)

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/swarmplot.png")
