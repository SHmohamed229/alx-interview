#!/usr/bin/python3
""" this Script Computes a Minimum Operations
"""


def minOperations(n):
    """
    this Method for Compute the minimum num
    of Operations

    Args:
        n: for input value
        factor_list: for List to save the operations
    Return: for the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
