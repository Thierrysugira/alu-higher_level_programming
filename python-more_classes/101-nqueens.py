#!/usr/bin/python3
"""Solves the N queens problem and prints every solution."""
import sys


def solve(n, row, cols):
    """Place queens row by row using backtracking.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row to fill.
        cols (list): The column of the queen placed in each previous row.
    """
    if row == n:
        print([[r, c] for r, c in enumerate(cols)])
        return
    for col in range(n):
        safe = True
        for r, c in enumerate(cols):
            if c == col or abs(c - col) == row - r:
                safe = False
                break
        if safe:
            cols.append(col)
            solve(n, row + 1, cols)
            cols.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, [])
