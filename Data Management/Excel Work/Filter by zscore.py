# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:43:14 2018

@author: james
"""

# Import zscore
from scipy.stats import zscore
import pandas as pd

file = ''
df = pd.read_csv(file)
    
# Group the df and standardize
standardized = df.groupby('')['',''].transform(zscore)

# Boolean series as an outlier as an identifier
outliers = (standardized[''] < -3) | (standardized[''] > 3)

# Filter the df by the outliers
gm_outliers = df.loc[outliers]
print(gm_outliers)

def function():
    return

# Group gapminder_2010 by 'region': regional
regional = df.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(function)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])


# Creates the 

# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10, 'pclass'])['survived'].mean()
print(survived_mean_2)

