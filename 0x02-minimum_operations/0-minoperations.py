#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    cal. the number of ops needed to result in n H x'ters
    exctly. If n is impossible to achieve, returns 0
    """
    if n < 2:
        return 0
    factor_list = []
    j = 1
    while n != 1:
        j += 1
        if n % j == 0:
            while n % j == 0:
                n /= j
                factor_list.append(j)
    return sum(factor_list)
