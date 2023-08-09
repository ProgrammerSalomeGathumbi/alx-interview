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

    # Initialize dp list to store minimum operations for each index
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with maximum operations
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]
