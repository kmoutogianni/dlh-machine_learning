#!/usr/bin/env python3
"""plotting exercise 3"""
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
def two():
    """plot x ↦ y1 and x ↦ y2 as line graphs"""
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.xlim(0, 20,000)
    plt.ylim(0, 1)

    plt.plot(y1, 'r--')
    plt.plot(y2, 'g-')

    plt.legend(loc = 'upper right')
    
two()

# %%
