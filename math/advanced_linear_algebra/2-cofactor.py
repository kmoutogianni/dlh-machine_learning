#!/usr/bin/env python3
"""Task 1 of advanced linear algebra"""


def cofactor(matrix):
    """calculates the cofactor matrix of a matrix"""

    # initial checks
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a list of lists")

    length = len(matrix)
    for i in range(length):
        row = matrix[i]
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(row) == 0 or len(row) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")

