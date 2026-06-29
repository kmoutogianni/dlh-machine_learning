#!/usr/bin/env python3
"""Task 3 of advanced linear algebra"""


def determinant(matrix):
    """calculates the determinant of a matrix"""

    # initial checks
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a list of lists")

    # 0x0 matrix
    if matrix == [[]]:
        return 1

    length = len(matrix)
    for i in range(length):
        row = matrix[i]
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(row) != len(matrix):
            raise ValueError("matrix must be a square matrix")

    # 1x1 matrix
    if length == 1:
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
        det += (-1) ** i * matrix[0][i] * determinant(minor)  # recursive calc

    return det


def adjugate(matrix):
    """calculates the adjugate matrix of a matrix"""

    # initial checks
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a list of lists")

    length = len(matrix)
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(row) == 0 or len(row) != length:
            raise ValueError("matrix must be a non-empty square matrix")

    # 1x1 matrix
    if length == 1:
        return [[1]]

    # all other matrices
    adjugate_matrix = []
    for j in range(length):          # for each column j
        adjugate_row = []     # create respective adjugate matrix row
        for i in range(length):      # for each row i
            # create minor matrix, and append the cofactor value to the row
            minor_matrix = []
            for k in range(length):
                if k != i:          # leave out row i
                    # leave out column j
                    minor_matrix.append(matrix[k][:j] + matrix[k][j+1:])
            adjugate_row.append((-1) ** (i+j) * determinant(minor_matrix))

        adjugate_matrix.append(adjugate_row)

    return adjugate_matrix
