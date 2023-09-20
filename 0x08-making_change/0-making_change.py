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
    else:
        coin = sorted(coins)
        coin.reverse()
        count = 0
    for c in coin:
        while total >= c:
            total -= c
            count += 1
        if total == 0:
            return count
    return -1
