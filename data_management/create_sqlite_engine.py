"""
Created on Tue Mar 13 08:20:22 2018

@author: James
"""

from sqlalchemy import create_engine


def get_tables_in_db():
    # Create an engine that connects to the census.sqlite file: engine
    engine = create_engine("sqlite:///census.sqlite")

    # Print table names
    print(engine.table_names())
    return engine.table_names()
