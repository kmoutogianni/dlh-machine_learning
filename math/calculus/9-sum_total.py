#!/usr/bin/env python3
"""exercise 9"""


def summation_i_squared(n):
    """calculates the sum of squares"""

    if n is not int:
        return None

    return n * (n + 1) * (2 * n + 1) // 6
