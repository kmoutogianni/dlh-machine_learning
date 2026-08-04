#!/usr/bin/env python3
"""task 1"""
import numpy as np


def correlation(C):
    """calculates a correlation matrix, given a covariance matrix"""

    if type(C) is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")
    if X.ndim != 2 or X.shape[0] != X.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std = np.sqrt(np.diag(C))
    correlation_matrix = C / np.outer(std, std)
    return correlation_matrix
