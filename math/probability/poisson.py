#!/usr/bin/env python3
"""task 0"""


class Poisson:
    """class representing a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """initiates with lambtha value"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the value of the PMF for k number of successes"""

        e = 2.7182818285

        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0

        factorial_k = 1
        for i in range(1, k+1):
            factorial_k = factorial_k * i

        P = self.lambtha**k * e**(-self.lambtha) / factorial_k
        return P
