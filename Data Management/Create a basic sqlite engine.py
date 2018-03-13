# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:20:22 2018

@author: James
"""

# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())

#next we need to try and load the data using reflection