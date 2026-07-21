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
