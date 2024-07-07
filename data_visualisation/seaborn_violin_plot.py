# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:47:29 2018

@author: James
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset that comes with seaborn
tips = sns.load_dataset('tips')

# Create a violinplot
sns.violinplot(x="day", y="total_bill", data=tips, inner=None)

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/violin_plot.png")
