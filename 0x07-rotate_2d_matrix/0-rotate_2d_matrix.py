#!/usr/bin/python3
"""
A module containing solution to
Rotate 2D Matrix 90% clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    rotate matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        start = 0
        end = n - 1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1
