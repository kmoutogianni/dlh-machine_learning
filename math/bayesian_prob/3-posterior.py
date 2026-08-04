#!/usr/bin/env python3
"""task 3"""

import numpy as np


def factorial(k):
    """calculates the factorial of k"""
    factorial_k = 1
    for i in range(1, k+1):
        factorial_k = factorial_k * i
    return factorial_k


def posterior(x, n, P, Pr):
    """calculates the posterior probability for the various
    hypothetical probabilities given the data"""

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
    if type(Pr) is not np.ndarray or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    n_choose_x = (factorial(n) // (factorial(x) * factorial(n-x)))
    L = n_choose_x * P**x * (1-P)**(n-x)  # likelihood
    intersection_array = L * Pr
    marginal_prob = np.sum(intersection_array)
    posterior_prob = intersection_array / marginal_prob
    return posterior_prob
