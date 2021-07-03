# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:29:17 2018

@author: James
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: fix the file import
filename = ""
df = pd.read_csv(filename)

# Creates a heatmap plotting the relationship between multiple variables
sns.heatmap(df)
plt.show()
