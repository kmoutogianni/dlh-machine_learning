#!/usr/bin/env python3
"""tasks 6-9"""


class Normal:
    """class representing a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """sets instance attributes mean and stddev"""

        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)

        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            n_samples = len(data)
            self.mean = sum(data) / n_samples

            var = 0
            for x in data:
                var += (x - self.mean)**2
            var = var / n_samples
            self.stddev = var ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""

        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""

        x = self.mean + z * self.stddev
        return x

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""
        pi = 3.1415926536
        e = 2.7182818285

        exp = -(x - self.mean)**2 / (2 * (self.stddev ** 2))
        f = 1 / (self.stddev * ((2*pi)**0.5)) * e ** exp
        return f
