#!/usr/bin/python3
"""
Module calculating perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Parameters:
    - grid (List[List[int]]): 2D grid (0 represents water, 1 represents land).

    Returns:
    - int: Perimeter of the island.
    """

    if not all(len(row) == len(grid[0]) for row in grid):
        return

    if not (1 <= len(grid) <= 100 and 1 <= len(grid[0]) <= 100):
        return

    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if row + 1 < rows and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col + 1 < cols and grid[row][col + 1] == 1:
                    perimeter -= 1
    return perimeter
