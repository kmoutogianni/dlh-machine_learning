#!/usr/bin/env python3
"""Module for Linear Algebra"""
import numpy as np

def np_elementwise(mat1, mat2):
    """performs element-wise calculations
    sum, difference, product, and quotient, respectively"""
    el1 = mat1 + mat2
    el2 = mat1 - mat2
    el3 = mat1 * mat2
    el4 = mat1 // mat2
    return el1, el2, el3, el4
