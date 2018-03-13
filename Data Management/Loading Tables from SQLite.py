# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:27:33 2018

@author: James
"""

# Import Table
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))
