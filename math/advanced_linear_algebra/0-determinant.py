#!/usr/bin/env python3
"""Task 0 of advanced linear algebra"""


def determinant(matrix):
    """calculates the determinant of a matrix"""

    # initial checks
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    else:
        length = len(matrix)

    for i in range(length):
        row = matrix[i]
        if row is not list:
            raise TypeError("matrix must be a list of lists")
        if len(row) != len(matrix):
            raise ValueError("matrix must be a square matrix")

    # empty matrix
    if matrix == [[]]:
        return 1

    # 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # other matrices
    det = 0
    for i in range(length):                     # for each column i
        minor = []                              # create the minor
        for row in matrix[1:]:                  # leave out first row
            minor.append(row[:i] + row[i+1:])   # leave out column i
        det += (-1) ^ i * matrix[0][i] * determinant(minor)  # recursive calc

    return det
