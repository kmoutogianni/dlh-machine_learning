#!/usr/bin/env python3
"""Module for Linear Algebra"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a specific axis"""

    if axis == 0:
        if len(mat1[0]) != len(mat2(0)):
            return None
        return mat1 + mat2

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
            
        new_matrix = []
        for i in range(len(mat1)):
            new_row = mat1[i] + mat2[i]
            new_matrix.append(new_row)
        return new_matrix
