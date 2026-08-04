#!/usr/bin/env python3
"""task 0"""

import numpy as np


def factorial(k):
    """calculates the factorial of k"""
    factorial_k = 1
    for i in range(1, k+1):
        factorial_k = factorial_k * i
    return factorial_k


def likelihood(x, n, P):
    """calculates the likelihood of x out of n patients developing side effects
    given various hypothetical probabilities given in array P"""

    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(P) is not np.ndarray or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    L = []  # list

    n_choose_x = (factorial(n) // (factorial(x) * factorial(n-x)))

    for p_value in P:
        if p_value < 0 or p_value > 1:
            raise ValueError("All values in P must be in the range [0, 1]")
        l_value = n_choose_x * p_value**x * (1-p_value)**(n-x)
        L.append(l_value)
    return np.array(L)  # 1D numpy array
