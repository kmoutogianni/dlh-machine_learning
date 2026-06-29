#!/usr/bin/env python3
"""Task 5 of advanced linear algebra"""

import numpy as np

def definiteness(matrix):

    if type(matrix) is not np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")

    # check if it is a 2-dim matrix
    if matrix.ndim != 2:
        return None

    # check if matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"

    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"

    if np.all(eigenvalues < 0):
        return "Negative definite"

    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    return "Indefinite"


mat1 = np.array([[5, 1], [1, 1]])
mat2 = np.array([[2, 4], [4, 8]])
mat3 = np.array([[-1, 1], [1, -1]])
mat4 = np.array([[-2, 4], [4, -9]])
mat5 = np.array([[1, 2], [2, 1]])
mat6 = np.array([])
mat7 = np.array([[1, 2, 3], [4, 5, 6]])
mat8 = [[1, 2], [1, 2]]

print(definiteness(mat1))
