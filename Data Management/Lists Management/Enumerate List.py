# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 07:04:29 2018

@author: James
"""

#creates an enumerator list which can be used to create an index of a list

data1 = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pride']

# Create a list of tuples: mutant_list
data1_list = list(enumerate(data1))

# Print the list of tuples
print(data1_list)

# Change the start index
for index2, value2 in enumerate(data1, start = 1):
    print(index2, value2)