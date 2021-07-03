# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 06:59:31 2018

@author: James
"""
import pandas as pd


def single_melt_csv_df(file_name: str, melt_col: str, val_col: str):
    df = pd.read_csv(file_name)

    # Reset the index
    df_reset = df.reset_index()

    # Melt visitors_by_city_weekday: visitors
    df_melt = pd.melt(df_reset, id_vars=[melt_col], value_name=val_col)

    # Print visitors
    print(df_melt)


def multi_col_melt(file_name, melt_list: list):
    df = pd.read_csv(file_name)
    # Multiple columns can be used as identifiers
    skinny = pd.melt(df, id_vars=melt_list)

    # Print skinny
    print(skinny)

    # Key-value pairs merge multi-index columns into one
    kv_pairs = pd.melt(df, col_level=0)
    print(kv_pairs)
