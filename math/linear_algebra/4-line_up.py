#!/usr/bin/env python3
"""Module for Linear Algebra"""


def add_arrays(arr1, arr2):
    """adds two arrays/lists element-wise"""

    if len(arr1) != len(arr2):
        return None

    new_arr = []
    for i in range(len(arr1)):
        new_arr.append(arr1[i] + arr2[i])

    return new_arr
