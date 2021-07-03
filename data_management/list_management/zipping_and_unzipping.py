# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 07:49:20 2018

@author: James
"""

data1 = (
    "charles xavier",
    "bobby drake",
    "kurt wagner",
    "max eisenhardt",
    "kitty pride",
)

data2 = ("bald", "unknown", "blue", "german?", "spooky")

# Create a zip object from data1 and data2: z1
z1 = zip(data1, data2)

# Print the tuples in z1 by unpacking with *
print(f"Unpacked zipped objects - {*z1,}")

# Unpacking a zipped object exhausts the zipped object
# Re-create a zip object from data1 and dat2: z1
z1 = zip(data1, data2)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
# This assigns the 1st list of data to result1 and the 2nd list to result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
if result1 == data1 and result2 == data2:
    print(f"Uncoupled objects {result1, result2}")
