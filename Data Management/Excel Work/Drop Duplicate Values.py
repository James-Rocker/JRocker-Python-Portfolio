# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:09:01 2018

@author: james
"""

""" Drop duplicates from a dataframe """

# Select columns: ev_gen
ev_gen = medals[["Event_gender", "Gender"]]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)
