# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:29:16 2018

@author: James
"""

import time

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
time.sleep(10)
