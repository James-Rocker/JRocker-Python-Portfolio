# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 05:49:21 2018

@author: James
"""

import pandas as pd 

filename = ''
df = pd.read_csv(filename)


# Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
between_values = (df.Edition >= 1952) & (df.Edition <= 1988)

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
df_is_in = df.NOC.isin(['', ''])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
df_filtered = df.loc[df_is_in & between_values]

# Group cold_war_medals by 'NOC'
df_groupedby = df_filtered.groupby('')

# Create Nsports
final_df = df_groupedby[''].nunique().sort_values(ascending=False)

# Print Nsports
print(final_df.head())
