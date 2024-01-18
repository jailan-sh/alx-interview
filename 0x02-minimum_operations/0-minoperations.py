#!/usr/bin/python3
"""
a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    n: n of H
    return: Returns an integer represent nh
    If n is impossible to achieve, return 0
    """
    if n == 1 or n == 0:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    if n > 1:
        operations += n

    return operations
