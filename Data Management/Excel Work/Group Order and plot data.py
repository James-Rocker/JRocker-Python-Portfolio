# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 06:21:33 2018

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt

filename = ""
df = pd.read_csv(filename)

# Redefine a column with a new order catergory
df.Medal = pd.Categorical(values=df.Medal, categories=["", "", ""], ordered=True)

# Create the DataFrame
df_filtered = df[df.NOC == "USA"]

# Group by columns
df_filtered_group = df_filtered.groupby(["", ""])[""].count()

# Reshape usa_medals_by_year by unstacking
df_filtered_group = df_filtered_group.unstack(level="")

# Create an area plot of usa_medals_by_year
df_filtered_group.plot.area()
plt.show()
