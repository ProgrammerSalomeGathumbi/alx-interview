#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0
    for x in range(len(grid)):
        for i in range(len(grid[x])):
            if grid[x][i] == 1:
                perimeter += 4
                if x > 0 and grid[x-1][i] == 1:
                    perimeter -= 2
                if i > 0 and grid[x][i-1] == 1:
                    perimeter -= 2
    return perimeter
