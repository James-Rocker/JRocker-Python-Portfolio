# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 07:00:20 2018

@author: James
"""

import pandas as pd

filename = ''
gdp = pd.read_csv(filename, parse_dates=True, index_col='')

# Slice all the data from x onward to create a new df
sliced_df = gdp['':]
print(sliced_df.tail(8))

# Resample by timeframe ('A' being annual yearly), keeping last()
resampled_df = sliced_df.resample('A').last()
print(resampled_df)

# Compute percentage growth of yearly to a new column
resampled_df['growth'] = resampled_df.pct_change() * 100
print(resampled_df)