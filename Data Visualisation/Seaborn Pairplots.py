# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:08:53 2018

@author: James
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = ""
df = pd.read_csv(filename)

sns.pairplot(df)
plt.show()

sns.pairplot(df, kind="reg", hue="origin")
plt.show()
