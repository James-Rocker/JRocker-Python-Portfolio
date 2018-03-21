# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:54:53 2018

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = ''
df=pd.read_csv(filename)

# Generate a joint plot
sns.jointplot(x='', y='', data=df)
plt.show()

# Generate a joint plot using a hexbin plot
sns.jointplot(data=df, x='', y='', kind='hex')
plt.show()