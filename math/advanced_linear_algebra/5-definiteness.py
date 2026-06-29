#!/usr/bin/env python3
"""Task 5 of advanced linear algebra"""

import numpy as np

def definiteness(matrix):
    """calculates the definiteness of a matrix"""

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
