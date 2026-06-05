#!/usr/bin/env python3
"""Module for Linear Algebra"""


def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    dims = []
    while type(matrix) is list:
        dim = len(matrix)
        dims.append(dim)
        matrix = matrix[0]

    return dims
