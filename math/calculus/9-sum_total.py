#!/usr/bin/env python3
"""exercise 9"""


def summation_i_squared(n):
    """calculates the sum of squares"""

    if type(n) is not int or n < 0:
        return None

    sum = n * (n + 1) * (2 * n + 1) / 6
    return int(sum)
