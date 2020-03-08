# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:59:32 2018

@author: james
"""
import pandas as pd
import numpy as np


def df_extract(file_name: str, filter_col):
    """Extracting data from a csv file"""
    df = pd.read_csv(file_name, index_col='')

    # Create the boolean array: high_turnout
    filter_val = df[filter_col] > 70

    # Filter the election DataFrame with the high_turnout array: high_turnout_df
    filter_val_df = df[filter_val]

    # Print the high_turnout_results DataFrame
    print(filter_val_df)


"""Filter a column based on another column"""


def filter_on_bool(file_name, filter_col):
    df = pd.read_csv(file_name, index_col='')

    print(df.head())
    # Create the boolean array: too_close
    filter_series = df[filter_col] < 1

    # Assign np.nan to the 'winner' column where the results were too close to call
    df.loc[filter_series, 'winner'] = np.nan

    # Print the output of election.info()
    print(filter_series.info())
