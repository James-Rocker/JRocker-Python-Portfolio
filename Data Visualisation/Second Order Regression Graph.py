# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:55:18 2018

@author: james
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('')

# Generate a scatter plot using red circles
plt.scatter(df[''], df[''], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='', y='', data=df, scatter=None, color='blue', label='order 1')

# Plot in green a linear regression
sns.regplot(x='', y='', data=df, scatter=None, order=2, color='green', label='order 2')

# Add lengend and display
plt.legend(loc='upper left')
plt.show()
