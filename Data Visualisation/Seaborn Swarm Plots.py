# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 07:34:36 2018

@author: James
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = ''
df=pd.read_csv(filename)

# Generate a swarm plot  
plt.subplot(2,1,1)
sns.swarmplot(y='', x='', data=df)

# Swarm plot of grouped data with a hue of 'origin' and horizontal orientation 
plt.subplot(2,1,2)
sns.swarmplot(x='', y='', data=df, hue='', orient='h')

# Display the plot
plt.show()
