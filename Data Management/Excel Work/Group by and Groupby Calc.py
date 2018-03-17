# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 07:50:02 2018

@author: James
"""

import pandas as pd

filename = ''
filename1 = ''
df = pd.read_csv(filename, index_col='')

# Single column grouping
df_group = df.groupby('').count()
print(df_group)

# Multi column grouping
df_multi = df.groupby(['','']).count()
print(df_multi)

# Reading 2 dataframes from csv files
df = pd.read_csv(filename, index_col='')
df1 = pd.read_csv(filename1, index_col='')

# Group a dataframe using the values of another column
df2 = df.groupby(df1[''])

# Calculating data based on the new grouped dataframe
print(df2[''].mean())

# 