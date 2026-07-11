#!/usr/bin/env python3
"""plotting exercise 0"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
def line():
    """plots y as a line graph"""

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.plot(y, 'r-')
    plt.show()
