# Tic-Tac-Toe in Python

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(" | ".join(board[0:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]))

# Function to check if the current player has won
def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def check_full():
    return " " not in board

# Main game loop
current_player = "X"
while True:
    print_board()
    print(f"Player {current_player}'s turn:")
    move = int(input("Enter your move (1-9): ")) - 1

    if move < 0 or move >= 9 or board[move] != " ":
        print("Invalid move. Try again.")
        continue

    board[move] = current_player

    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if check_full():
        print_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
