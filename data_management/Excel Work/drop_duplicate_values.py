# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:09:01 2018

@author: james
"""
import pandas as pd

# Select columns: ev_gen
ev_gen = pd.DataFrame(["Event_gender", "Gender", "Gender"])

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)
