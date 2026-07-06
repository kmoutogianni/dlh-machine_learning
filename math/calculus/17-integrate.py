#!/usr/bin/env python3
"""exercise 17"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""

    if type(poly) is not list:
        return None
    if type(C) is not int:
        return None
    if len(poly) == 0:
        return None

    new_poly = []
    new_poly.append(C)
    for i in range(1, len(poly)+1):
        new_poly.append(poly[i-1] / i)
    return new_poly
