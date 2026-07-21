#!/usr/bin/env python3
"""tasks 10-12"""


class Binomial:
    """class representing a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Sets the instance attributes n and p"""

        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")

            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")

            self.n = int(n)
            self.p = float(p)

        else:
            if type(data) is not list:
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)

            var = 0
            for x in data:
                var += (x - mean)**2
            var = var / len(data)

            p = 1 - var / mean
            n = mean / p
            n = round(n)

            self.n = int(n)
            self.p = float(mean / self.n)

        def pmf(self, k):
            """Calculates the value of the PMF for k number of successes"""

            if type(k) is not int:
                k = int(k)
            if k < 0:
                return 0

            factorial_n = 1
            for i in range(1, self.n + 1):
                factorial_n *= i

            factorial_k = 1
            for i in range(1, k + 1):
                factorial_k *= i

            factorial_n_k = 1
            for i in range(1, self.n - k + 1):
                factorial_n_k *= i

            comb_n_k = factorial_n / (factorial_k * factorial_n_k)
            P = comb_n_k * p ** k * (1-p) ** (n-k)
            return p
