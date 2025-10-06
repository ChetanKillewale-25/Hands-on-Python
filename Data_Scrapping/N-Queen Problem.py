def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1

    return True

def solve_n_queens(board, col, n):
    # base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col then return false
    return False

def solve(n):
    board = [[0]*n for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")
        return False

    print_board(board, n)
    return True

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()

# Driver code
n = 6
solve(n)
