"""
Created on Tue Mar 13 08:27:33 2018

@author: James
"""

from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer


def create_micro_db(table_name: str):
    # Create an engine that connects to the census.sqlite file: engine
    engine = create_engine("sqlite:///micro_db.sqlite", echo=True)
    metadata = MetaData()

    # Reflect the selected table from the engine: micro_db
    census = Table(table_name, metadata, Column("id", Integer, primary_key=True))
    metadata.create_all(engine)


# TODO: Fix whatever this is supposed to show
