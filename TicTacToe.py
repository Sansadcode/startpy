def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for row in board:
        print(" | ".join(str(cell) for cell in row))
        print("-" * 5)
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move! Please choose a number between 1 and 9.")
            else:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == 'X' or board[row][col] == 'O':
                    print("Cell is already occupied! Choose another.")
                else:
                    board[row][col] = 'O'
                    break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 9.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('X', 'O'):  # Cell is free if it's not 'X' or 'O'
                free_fields.append((row, col))

    return free_fields
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


import random


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)  # Select a random free square
        board[row][col] = 'X'  # Computer places 'X' in the selected square
def play_game():
    # Initialize the board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    display_board(board)

    while True:
        # User's move
        enter_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        # Computer's move
        draw_move(board)
        display_board(board)

        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# Run the game
play_game()
