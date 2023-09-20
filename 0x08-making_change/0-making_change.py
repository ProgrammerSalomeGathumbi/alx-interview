#!/usr/bin/python3
"""
Making changes
"""


def makeChange(coins, total):
    """
    determine the fewest coins needed to meet a total
    """
    if total < 1:
        return 0
    c_list = [float('inf')] * (total + 1)
    c_list[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            c_list[i] = min(c_list[i], c_list[i - coin] + 1)

    if c_list[total] != float('inf'):
        return c_list[total]
    else:
        return -1
