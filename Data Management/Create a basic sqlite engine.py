# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:20:22 2018

@author: James
"""

import imp, pip 
from time import sleep


def install_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print('Error ' + package + ' library is missing ')
        var = input("Do you want to download and install the " + package + " library?")
        if var in ['no', 'n', 'No', 'N', 'NO']:
            print('Error, ' + package + ' not installed.')
            sleep(5)
            quit()
        else:
            pip.main(['install', package])


packagelist = ['sqlalchemy']
for x in packagelist:
    install_func(x)

# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())

# Next we need to try and load the data using reflection
