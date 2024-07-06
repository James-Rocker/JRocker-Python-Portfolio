# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:08:57 2018

@author: james
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load the example dataset
df = sns.load_dataset('tips')

# Create box plot with Seaborn's default settings
sns.boxplot(data=df, x='day', y='total_bill')

# Label the axes
plt.xlabel("day")
plt.ylabel("total bill")

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/box_and_whisker.png")
