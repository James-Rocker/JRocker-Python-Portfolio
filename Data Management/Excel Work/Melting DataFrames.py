# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 06:59:31 2018

@author: James
"""
import pandas as pd

filename = ''
df = pd.read_csv(filename)

# Melting
# Reset the index: visitors_by_city_weekday
df_reset = df.reset_index() 

# Print visitors_by_city_weekday
print(df_reset)

# Melt visitors_by_city_weekday: visitors
df_melt = pd.melt(df_reset, id_vars=[''], value_name='')

# Print visitors
print(df_melt)

# Multiple columns can be used as identifiers
skinny = pd.melt(df, id_vars=['', ''])

# Print skinny
print(skinny)

# Key-value pairs merge multiindex columns into one
kv_pairs = pd.melt(df, col_level=0)