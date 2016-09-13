"""
bootcamp_utils: a collection of statistical functions
"""

import numpy as np


def ecdf(data):
    """
    Compute x, y values for an empirical distribution.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y
