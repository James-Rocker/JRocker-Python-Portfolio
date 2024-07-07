# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:29:17 2018

@author: James
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

# Create a heatmap of tip percentage vs day of the week and time of day
plt.figure(figsize=(10, 8))
sns.heatmap(
    tips.pivot_table(
        values="tip", index="day", columns="time", aggfunc="mean", observed=False
    ),
    cmap="Blues",
    annot=True,
)

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/heatmap_graph.png")
