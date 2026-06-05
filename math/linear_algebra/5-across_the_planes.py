#!/usr/bin/env python3
"""Module for Linear Algebra"""


def add_matrices2D(mat1, mat2):
    """adds two 2D matrices element-wise"""

    if len(mat1) != len(mat2):
        return None

    if len(mat1[0]) != len(mat2[0]):
        return None

    new_matrix = []

    new_row = []
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            new_row.append(mat1[i][j] + mat2[i][j])

    new_matrix.append(new_row)

    return new_matrix
