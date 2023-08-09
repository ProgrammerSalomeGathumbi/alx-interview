#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    i = 0
    j = 2
    while n > 1:
        while n % j == 0:
            i += j
            n //= j
        j += 1
    return i
