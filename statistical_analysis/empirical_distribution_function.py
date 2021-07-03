"""
Created on Sat July 25 06:45:12 2021

@author: James
"""


from typing import Any, Tuple
import numpy as np


def empirical_dist(data: np.ndarray[Any, Any]) -> Tuple: # pylint: disable=E1136
    """
    Takes a numpy array arg, creates a sorted array as the x_axis and y_axis for a numpy array
    Then return the two numpy arrays as a tuple
    """
    list_count = data.size
    x_axis = np.sort(data)

    # we are dividing here because it makes visualising larger arrays easier
    y_axis = np.arange(1, list_count + 1) / list_count
    return x_axis, y_axis
