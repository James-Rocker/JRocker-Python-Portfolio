# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:51:22 2017

@author: James
"""

input = input('Enter the numbers to remove odds from (e.g. 2 3 4): ' )
userinput = input.split()
userinput = [int(a) for a in userinput] 

def purify(numbers):
    d = []
    for c in numbers:
        if c % 2 == 0:
            d.append(c)
    return d     
output = purify(userinput)
print (output)
