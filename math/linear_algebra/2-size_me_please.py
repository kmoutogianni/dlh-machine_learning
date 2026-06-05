#!/usr/bin/env python3

def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    dims = []
    while type(matrix) is list:
        dim = len(matrix)
        dims.append(dim)
        matrix = matrix[0]

    print(dims)
