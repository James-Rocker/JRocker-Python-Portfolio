# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 05:38:43 2018

@author: James
"""

# Grouping data, get unique vales and sort them

import pandas as pd 

filename = ''
df = pd.read_csv(filename)

# Group the data
df_grouped = df.groupby([''])

# Compute the number of distinct values
df_sorted = df_grouped[''].nunique()

# Sort the values in descending order
df_sorted = df_sorted.sort_values(ascending=False)

# Print the top 15 rows
print(df_sorted.head(15))
