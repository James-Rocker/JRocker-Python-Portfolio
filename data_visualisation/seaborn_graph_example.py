# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:05:55 2018

@author: james
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

example = {
    "Column 1": [1, 2, 5, 3, 7],
    "Column 2": [5, 7, 1, 2, 5],
    "Column 3": [7, 2, 5, 4, 1],
}
example = pd.DataFrame(example, index=["A", "B", "C", "D", "E"])

# Create violin plot
sns.swarmplot(x="A", y="Column 3", data=example)  # TODO: fix this

# Show the plot
plt.show()
