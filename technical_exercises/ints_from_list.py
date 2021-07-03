# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:15:34 2018

@author: James
"""

list_of_stuff = [9, 10, 10.1, 19.2, 4.3, 0, "test"]
to_int = [x for x in list_of_stuff if isinstance(x, int)]
print(to_int)
