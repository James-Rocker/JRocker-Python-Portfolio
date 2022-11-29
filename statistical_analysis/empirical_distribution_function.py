"""
Created on Sat July 25 06:45:12 2021

@author: James
"""


from typing import Any, Tuple
import numpy as np


def empirical_dist(data: np.ndarray[Any, Any]) -> Tuple:
    """
    Takes a numpy array arg, creates a sorted array as the x_axis and y_axis for a numpy array
    Then return the two numpy arrays as a tuple object to split it later
    """
    # we use numpy size method because it calculates total number of elements vs len which is just the first dimension
    list_count = data.size
    x_axis = np.sort(data)  # we want to graph this data later, so we need this sort

    # returns evenly spaced values within a given interval. These should be ints, for decimals use np.linspace
    y_axis = np.arange(start=1, stop=list_count + 1) / list_count  # divide here, so we always keep the y-axis max of 1
    return x_axis, y_axis
