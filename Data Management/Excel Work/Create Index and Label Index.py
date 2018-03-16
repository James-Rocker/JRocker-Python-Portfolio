# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:47:09 2018

@author: james
"""
import pandas as pd
filename = ''

df = pd.read_csv(filename, index_col='')

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index thus generating an index for the dataframe
df.index = months

# Print the modified sales DataFrame
print(df)

#Add an index name to a dataframe
# Assign the string 'MONTHS' to sales.index.name
df.index.name = 'MONTHS'

# Print the sales DataFrame
print(df)

# Assign the string 'PRODUCTS' to sales.columns.name 
df.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(df)


