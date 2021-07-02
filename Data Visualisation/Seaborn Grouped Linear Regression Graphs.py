# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:41:26 2018

@author: james
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("")

# Plot linear regressions grouped row-wise
sns.lmplot(x="", y="", data=df, row="")
plt.show()

sns.lmplot(data=df, x="", y="", hue="", palette="Set1")
plt.show()

# Strip plot
plt.subplot(2, 1, 1)
sns.stripplot(x="", y="", data=df)

# Strip plot using jitter and a smaller point size
plt.subplot(2, 1, 2)
sns.stripplot(x="", y="", jitter=True, data=df, size=3)
plt.show()
