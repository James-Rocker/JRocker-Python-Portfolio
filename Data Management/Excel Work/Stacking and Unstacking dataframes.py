# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 06:07:26 2018

@author: James
"""

import pandas as pd 

filename = ''
df = pd.read_csv(filename)

filename1 = ''
df1 = pd.read_csv(filename1)

# Stack the data (grouping the data)
# By stacking the data, we use less columns but more rows
df = df.stack(level='county')
print(df)

# Unstack 
df = df.unstack(level='county')
print(df)

# By stacking and unstacking the data is stacked by different levels
# Now we are going to change the index using swaplevel

# Swap the levels of the index of newusers: newusers
df1 = df.swaplevel(0, 1)

# Print newusers and verify that the index is not sorted
print(df1)

# Sort the index of newusers: newusers
df1 = df1.sort_index()

# Print newusers and verify that the index is now sorted
print(df1)

# Test that the dataframe is equal to another 
print(df.equals(df1))