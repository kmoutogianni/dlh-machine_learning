#!/usr/bin/env python3
"""Module for Linear Algebra"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""

    if len(mat1[0]) != len(mat2):
        return None

    new_matrix = []
    for i in range(len(mat1)):   # for each row in mat1
        new_row = []
        for j in range(len(mat2[0])):   # for each col in mat2
            c = 0
            for k in range(len(mat2)):  # calculate the dot product
                c += mat1[i][k] * mat2[k][j]
            new_row.append(c)
        new_matrix.append(new_row)  # add the result row

    return new_matrix
