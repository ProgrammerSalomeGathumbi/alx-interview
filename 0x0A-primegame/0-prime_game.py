#!/usr/bin/python3
"""
Prime Game
"""


def isPrimeNumber(n):
    """
    generates a list of prime numbers
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for x in range(p * p, n + 1, p):
                primes[x] = False
        p += 1
    return [x for x in range(n + 1) if primes[x]]


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    primes = isPrimeNumber(max(max(nums), 1))
    Maria = 0
    Ben = 0
    for n in nums:
        if n == 1 or (n - 1) % 4 == 0:
            Ben += 1
        elif n in primes:
            Maria += 1
        else:
            Ben += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
