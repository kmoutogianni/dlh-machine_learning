#!/usr/bin/env python3
"""plotting exercise 6"""
# %%
import numpy as np
import matplotlib.pyplot as plt


def bars():
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # your code here
    person = np.arange(3)

    plt.bar(person,
            fruit[0],
            width=0.5,
            color="red",
            label="apples")

    plt.bar(person,
            fruit[1],
            width=0.5,
            bottom=fruit[0],
            color="yellow",
            label="bananas")

    plt.bar(person,
            fruit[2],
            width=0.5,
            bottom=fruit[0] + fruit[1],
            color="#ff8000",
            label="oranges")

    plt.bar(person,
            fruit[3],
            width=0.5,
            bottom=fruit[0] + fruit[1] + fruit[2],
            color="#ffe5b4",
            label="peaches")

    plt.xticks(["Farrah", "Fred", "Felicia"])
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.ylabel('Quantity of Fruit')

    plt.legend()
    plt.show()


bars()

# %%
