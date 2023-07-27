#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    # Initialize the first row with a single element, which is 1
    triangle = [[1]]

    for x in range(1, n):
        # The current row depends on the previous row
        # Start with the first element (1).
        row = [1]

        for i in range(1, x):
            # The elements in between are the sum of the \
            # two numbers above them in the previous row.
            row.append(triangle[x - 1][i - 1] + triangle[x - 1][i])
        # end row with 1
        row.append(1)
        # add the completed row in the triangle
        triangle.append(row)
    return triangle
