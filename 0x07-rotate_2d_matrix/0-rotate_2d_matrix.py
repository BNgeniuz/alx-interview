#!/usr/bin/python3
""" doc doc doc """


def rotate_2d_matrix(matrix):
    """doc doc doc"""
    n = len(matrix)

    for v in range(n):
        for w in range(v, n):
            matrix[w][v], matrix[v][w] = matrix[v][w], matrix[w][v]

    for v in range(n):
        matrix[v] = matrix[v][::-1]
