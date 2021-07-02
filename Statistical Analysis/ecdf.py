# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 08:14:18 2018

@author: James
"""
import numpy as np


def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y
