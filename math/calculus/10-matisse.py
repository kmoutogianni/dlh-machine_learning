#!/usr/bin/env python3
"""exercise 10"""


def poly_derivative(poly):
    """calculates the derivative of a polynomial"""

    # if poly not valid
    if type(poly) is not list:
        return None
    if len(poly) == 0:
        return None
    for element in poly:
        if type(element) is not int:
            return None

    # if the derivative is 0
    if len(poly) == 1:
        deriv_poly = [0]
        return deriv_poly

    # calculate derivative polynomial
    deriv_poly = []
    for i in range(1, len(poly)):
        d = poly[i] * i
        deriv_poly.append(d)
    return deriv_poly
