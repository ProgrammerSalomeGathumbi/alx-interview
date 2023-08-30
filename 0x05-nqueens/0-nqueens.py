#!/usr/bin/python3
"""
0. N queens
"""
import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(N):
    solutions = []

    def solve_util(board, col):
        nonlocal solutions
        if col >= N:
            solutions.append([(r, c.index(1))
                             for r, c in enumerate(board)])
            return
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve_util(board, col + 1)
                board[i][col] = 0
    initial_board = []
    for _ in range(N):
        initial_board.append([0] * N)
    solve_util(initial_board, 0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[r, c] for r, c in solution]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
