# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:53:59 2018

@author: james
"""

# Create a list of strings: fellowship
fellowship = ["frodo", "samwise", "merry", "aragorn", "legolas", "boromir", "gimli"]

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(f"The original fellowship - {new_fellowship}")

new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]
print(
    f"Only showing members if their name has or has more than 7 characters - {new_fellowship}"
)

new_fellowship = {member: len(member) for member in fellowship}

print(f"Showing members as a key, with their name length as a value - {new_fellowship}")
