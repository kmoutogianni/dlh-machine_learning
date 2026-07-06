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
    if poly != [0]:
        for i in range(1, len(poly)+1):
            c = poly[i-1] / i
            if c % 1 == 0:
                c = int(c)
            new_poly.append(c)
    return new_poly
