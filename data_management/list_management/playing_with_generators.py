# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:04:11 2018

@author: james
"""
# Create a list of strings
lannister = ["cersei", "jaime", "tywin", "tyrion", "joffrey"]

print('In this exercise, we are getting the length of each object in a list and using a '
      'generator to output the result')
print(lannister)
print('Create a generator object without using yield')
lengths = (len(person) for person in lannister)

# Iterate over the generator to return the value
for value in lengths:
    print(value)


# Define generator function get_lengths
def get_lengths(input_list: list):
    """
    Generator function that yields the length of the strings in input_list
    """
    for person in input_list:
        yield len(person)


# Print the values generated by get_lengths()
print('Using the built in yield method')
for value in get_lengths(lannister):
    print(value)