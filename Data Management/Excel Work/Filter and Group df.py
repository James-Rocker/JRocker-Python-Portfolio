# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 05:49:21 2018

@author: James
"""

import pandas as pd 


def filter_csv(filename: str, year_col):
    df = pd.read_csv(filename)

    # Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
    between_values = (df[year_col] >= 1952) & (df[year_col] <= 1988)

    # Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
    df_is_in = df.NOC.isin(['', ''])

    # Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
    df_filtered = df.loc[df_is_in & between_values]
    return df_filtered


def group_df(df):
    # Group cold_war_medals by 'NOC'
    df_grouped_by = df.groupby('')

    # Create N sports
    final_df = df_grouped_by[''].nunique().sort_values(ascending=False)

    # Print N sports
    print(final_df.head())
