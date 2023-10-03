#!/usr/bin/python3
"""
Prime Game
"""


def isPrimeNumber(n):
    """
    generates a list of prime numbers
    """
    primes = []
    primeNos = [True] * (n + 1)
    for prime in range(2, n + 1):
        if primeNos[prime]:
            primeNos.append(prime)
            for x in range(prime, n + 1, prime):
                primeNos[x] = False
    return primes


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for n in range(x):
        primes = isPrimeNumber(nums[n])
        if len(primes) == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
