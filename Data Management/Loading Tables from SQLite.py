"""
Created on Tue Mar 13 08:27:33 2018

@author: James
"""

from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite', echo=True)
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata,
               Column('id', Integer, primary_key=True))
metadata.create_all(engine)

