"""
Created on Thu Mar 22 07:00:20 2018

@author: James
"""

import pandas as pd


def csv_time_percent_change(filename: str):
    gdp = pd.read_csv(filename, parse_dates=True, index_col="")

    # Slice all the data from x onward to create a new df
    sliced_df = gdp["":]
    print(sliced_df.tail(8))

    # Re_sample by time frame ('A' being annual yearly), keeping last()
    re_sampled_df = sliced_df.resample("A").last()
    print(re_sampled_df)

    # Compute percentage growth of yearly to a new column
    re_sampled_df["growth"] = re_sampled_df.pct_change() * 100
    return re_sampled_df
