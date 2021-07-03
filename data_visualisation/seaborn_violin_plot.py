# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:47:29 2018

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = ""
df = pd.read_csv(filename)

# Generate a violin plot
plt.subplot(2, 1, 1)
sns.violinplot(x="", y="", data=df)

# Generate the same violin plot with a color of 'lightgray' without annotations
# Strip plot to overlay the violin diagram
plt.subplot(2, 1, 2)
sns.violinplot(x="", y="", data=df, inner=None, color="lightgray")
sns.stripplot(x="", y="", data=df, jitter=True, size=1.5)

# Display the plot
plt.show()
