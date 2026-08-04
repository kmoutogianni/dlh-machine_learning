#!/usr/bin/env python3
"""task 2"""
import numpy as np


class MultiNormal:
    """class representing a Multivariate Normal distribution"""

    def __init__(self, data):
        """constructor setting mean and cov public instance variables"""

        if type(data) is not np.ndarray or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        mean = np.mean(data, axis=1, keepdims=True)

        data_centered = data - mean

        cov = (data_centered @ data_centered.T) / (n - 1)

        self.mean = mean
        self.cov = cov
