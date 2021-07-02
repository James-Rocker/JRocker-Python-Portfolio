# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:25:19 2018

@author: james
"""
import pandas as pd

filename = ""

"""Extracting data from a csv file"""
df = pd.read_csv(filename, index_col="")

# Create the list of row labels: rows
rows = ["", "", ""]

# Create the list of column labels: cols
cols = ["", "", ""]

# Create the new DataFrame: three_counties
results = df.loc[rows, cols]

# Print the three_counties DataFrame
print(results)
