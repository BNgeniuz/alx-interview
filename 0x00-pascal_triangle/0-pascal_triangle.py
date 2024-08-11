#!/usr/bin/python3

"""Solves the interview problem"""


def pascal_triangle(n):
    """Prints pascal triangle based on value of n"""
    triangle = []

    for k in range(n):
        firm = []

        if k == 0:
            firm = [1]
            triangle.append(firm)
        elif k == 1:
            firm = [1, 1]
            triangle.append(firm)
        else:
            firm = [1]
            last_value = triangle[len(triangle) - 1]
            for l in range(len(last_value) - 1):
                firm.append(last_value[l] + last_value[l+1])
            firm.append(1)
            triangle.append(firm)

    return triangle
