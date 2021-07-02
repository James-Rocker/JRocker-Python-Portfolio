# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:15:34 2018

@author: James
"""

x = [9, 10, 10.1, 19.2, 4.3, 0, 'test']
to_int = [i if type(i) == int else int(i) for i in x]
print(to_int)