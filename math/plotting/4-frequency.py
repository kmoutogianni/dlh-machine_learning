#!/usr/bin/env python3
"""plotting exercise 4"""
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
def frequency():
    """ plot a histogram of student scores for a project"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    plt.xlim(0, 100)
#    plt.yticks(np.arange(0, 35, 5))
#    plt.xticks(np.arange(0, 101, 10))
    bins = np.arange(0, 101, 10)  # bins every 10 units
    plt.title('Project A')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.hist(student_grades, bins=bins, edgecolor='black')
    plt.show()

# %%
