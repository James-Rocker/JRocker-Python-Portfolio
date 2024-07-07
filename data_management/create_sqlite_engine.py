"""
Created on Tue Mar 13 08:20:22 2018

@author: James
"""

from sqlalchemy import create_engine, inspect


def get_tables_in_db():
    # Create an engine that connects to the census.sqlite file: engine
    engine = create_engine("sqlite:///census.sqlite")

    # using the slightly newer run time inspection module
    engine_inspection = inspect(engine)
    table_names = engine_inspection.get_table_names()
    # Print table names
    return table_names


print(get_tables_in_db())
