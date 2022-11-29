# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 08:28:14 2018

@author: James
"""

import pandas as pd

data = []
data_types = ["ints", "strings", "boolean"]

for data in data_types:

    # File name based on wildcard filename
    file_name = "%s_top5.csv" % data

    # Create list of column names: columns
    columns = ["Data type", data]

    data_df = pd.read_csv(file_name, header=0, index_col="Data type", names=columns)
    data.append(data_df)

# Concatenate
data = pd.concat(data, axis="columns")
data["new_column"] = "silly message"
print(data)
