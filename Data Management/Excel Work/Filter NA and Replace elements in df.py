# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:57:10 2018

@author: james
"""

import pandas as pd

filename = ""

df = pd.read_csv(filename, index_col="")

# Select the columns: df
df = df[["age", "cabin"]]

# Print the shape of df
print(df.shape)

""" Drop rows in df with how='any'. 
This will drop the row if any values are na while all drops if all rows are na"""
print(df.dropna(how="any").shape)
print(df.dropna(how="all").shape)

# Drop column if 1000 values are na
print(df.dropna(thresh=1000, axis="columns").info())

# Applying a function to every element in a column
def to_celsius(F):
    return 5 / 9 * (F - 32)


# Apply the function over the columns
df_celsius = df[["Mean TemperatureF", "Mean Dew PointF"]].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ["Mean TemperatureC", "Mean Dew PointC"]

# Print the output of df_celsius.head()
print(df_celsius.head())
