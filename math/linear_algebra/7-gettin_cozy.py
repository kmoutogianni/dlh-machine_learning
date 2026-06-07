#!/usr/bin/env python3
"""Module for Linear Algebra"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a specific axis"""

    if axis == 0:
        return mat1 + mat2

    if axis == 1:
        new_matrix = []
        for i in range(len(mat1)):
            new_row = mat1[i] + mat2[i]
            new_matrix.append(new_row)
        return new_matrix
