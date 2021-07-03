# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 17:59:09 2018

@author: james
"""

import pandas as pd

filename = ""

df = pd.read_csv(filename, index_col="")

# Pivot the users DataFrame: visitors_pivot
pivot = df.pivot(index="", columns="", values="")

# Print the pivoted DataFrame
print(pivot)

# Functions can also be applied to objects in a dataframe
calculated = df.pivot(index="", columns="", values="", aggfunc=sum)
print(calculated)

# We can aggregate and summerize data as well
Total = df.pivot_table(index="", aggfunc=sum, margins=True)
print(Total)
