#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""

import sys


def is_safe(board, row, column):
    """
    Check if placing a queen at a given position is safe.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        column (int): The columnumn index to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """

    for i in range(row):
        if board[i] == column or board[i] - i == column - row \
                or board[i] + i == column + row:
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and find all possible solutions.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of all possible solutionsas a list of queen positions.
    """

    board = [-1] * n
    solutions = []

    def place_queen(row):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
        else:
            for column in range(n):
                if is_safe(board, row, column):
                    board[row] = column
                    place_queen(row + 1)

    place_queen(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)
