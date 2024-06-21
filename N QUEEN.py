def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queen_util(board, row, n):
    # If all queens are placed
    if row >= n:
        return True

    # Try placing queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            # Recur to place rest of the queens
            if solve_n_queen_util(board, row + 1, n):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, then backtrack
            board[row][col] = 0

    # If the queen cannot be placed in any column in this row, then return False
    return False

def solve_n_queen(n):
    board = [[0] * n for _ in range(n)]
    if solve_n_queen_util(board, 0, n):
        print_board(board)
    else:
        print("No solution exists.")

# Example usage
solve_n_queen(8)  # Solves the 8-queen problem
