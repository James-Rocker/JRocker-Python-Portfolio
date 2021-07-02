# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:18:37 2018

@author: james
"""

import matplotlib.pyplot as plt
import pandas as pd

filename = ""
df = pd.read_csv(filename)

# Slice the df from two dates
view = df["":""]

# Plot the entire series
plt.plot(view)
plt.xticks(rotation=45)
plt.title("")
plt.axes([0.25, 0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color="red")
plt.xticks(rotation=45)
plt.title("")
plt.show()
