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
    i = 0  # Initialize the count of operations to 0
    j = 2  # Start with the smallest prime divisor
    while n > 1:
        while n % j == 0:
            i += j  # Add the divisor to the operations count
            n //= j  # Reduce n by the divisor
        j += 1  # Move to the next divisor
    return i
