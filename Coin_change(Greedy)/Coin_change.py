"""
Statement:
You are a cashier at a store. You need to give a customer n amount of change using the fewest number of coins possible.
You have an infinite supply of coins of denominations: {1, 2, 5, 10, 20, 50, 100, 500, 2000}.
Write an algorithm that takes an integer n and returns the list of coins that make up that change using a Greedy approach.
"""

from typing import List


def coinchange(n: int) -> list:
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]

    coins.sort(reverse=True)
    amount = n
    i = 0
    res = []
    while amount != 0:
        if coins[i] <= amount:
            amount = amount - coins[i]
            res.append(coins[i])

        else:
            i += 1
    return res


print(coinchange(500))
