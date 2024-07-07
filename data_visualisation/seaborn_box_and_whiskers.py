# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:08:57 2018

@author: james
"""

import seaborn as sns
import matplotlib.pyplot as plt

# load the example dataset
df = sns.load_dataset("tips")

# Let's inspect the data
print(df.head())

# set the graph style. List of possible choices comes from the `set_style` function in `rcmod.py`
sns.set_style(style="dark")
# set the palette. List of possible choices comes from the color_palette function in seaborn `palettes.py`
sns.set_palette(palette="deep")

# We want to sort the day order by the most amount of sales. We need another dataframe to represent that
total_cost = df[["total_bill", "day"]]
total_cost = total_cost.groupby(by=["day"])["total_bill"].sum().reset_index()
sorted_total_cost = total_cost.sort_values("total_bill", ascending=False)

# Create box plot with Seaborn's default settings. Let's also compare the smokers as well
sns.boxplot(
    data=df, x="day", y="total_bill", hue="smoker", order=sorted_total_cost["day"]
)

# Label the axes
plt.xlabel("day")
plt.ylabel("total bill")

# setting the title
plt.title("Tips by Day")

# Show the plot, disabling here because I'm using a headless console
# plt.show()
plt.savefig("graph_output/box_and_whisker.png")
