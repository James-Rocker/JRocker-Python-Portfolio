# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 08:01:48 2018

@author: James
"""
import pandas as pd

""" When working with large datasets, instead of processing everything all at once,
we work with a couple of items at a time using for loops
"""

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('', 10, '')

# Print result_counts
print(result_counts)
