#!/usr/bin/env python3
"""Module for Linear Algebra"""


def matrix_transpose(matrix):
    """returns the transpose of a 2D matrix"""
    transposed = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[col])

        transposed.append(new_row)
    return transposed
