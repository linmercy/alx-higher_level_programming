#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at position (row, col)."""
    # Check the row on the left side
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def print_solution(board):
    """Print the N queens solution."""
    result = [[i, board[i]] for i in range(len(board))]
    print(result)

def solve_nqueens(board, col, N):
    """Recursively solve the N queens problem."""
    if col == N:
        print_solution(board)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = row
            solve_nqueens(board, col + 1, N)

def nqueens(N):
    """Main function to solve the N queens problem."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])

