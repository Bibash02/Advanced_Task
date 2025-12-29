

# Function to display the chessboard
def print_board(board):
    print("Solution: \n")
    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Check whether a queen can be placed at board[row][col]
def is_safe(board, row, col, n):
    # Check column (upper side)
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    i, j = row, col
    # Check upper left diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
        return True

# Solving the N-Queens problem using backtracking 
def solve_n_queens(board, row, n):
    # If all queens are placed
    if row == n:
        return True
    
    # Try placing queen in all columns of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            
            # Recur to place rest of queens
            if solve_n_queens(board, row + 1, n):
                return True
            
            board[row][col] = 0 # BackTrack
    return False

# main function
def n_queens():
    n = int(input("Enter the value of N: "))

    if n < 1:
        print("Invalid input! N must be greater then 0.")
        return
    
    # Initialize chessboard with 0
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists for N = ", n)

n_queens()
