import random

print("Hey there, welcome to my Tic Tac Toe showdown")

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def draw_board():
    '''
    Output the Tic Tac Toe board with borders and values
    '''
    # Loop through each row of the game board
    for row in board:
        print('+---+---+---+')
        # Print the content of the row, joining values with ' | '
        print('|', end=' ')
        print(' | '.join(row), end=' ')
        # End the row with a border and a new line
        print('|')
    # Print the bottom border of the board to complete the visual representation
    print('+---+---+---+')


def get_next_move():
    '''
    Prompt the user to input their next move for the Tic Tac Toe game.
    Returns:
        - int. User's valid move (an integer between 1 and 9).
    '''
    # Prompt user for input until a valid move is provided.
    while True:
        try: 
            next_move = int(input("What's your move, superstar? Pick a number from 1 to 9: "))
            if validate_move(next_move):
                return next_move
        # It handles non-numeric input
        except ValueError:
            print("Oops, that's not a valid move. Try again, champ!")


def validate_move(move):
    '''
    Validate a user's move for the Tic Tac Toe game.

    Parameters:
    - move (int). The user's move to be validated.

    Returns:
    - bool. True if the move is valid, False if it's not.
    '''
    if move < 1 or move > 9:
        # Print out-of-range moves
        print(f"{move}'s out of range, champ. Pick a number from 1 to 9.")
        return False
    row, col = divmod(move - 1, 3)
    # Checks if position is not already tanken
    if board[row][col] in ['X', 'O']:
        # Print error message
        print("Oops, that spot's taken, buddy!")
        return False
    return True


def update_board(board, move, mark):
    '''
    Update the Tic Tac Toe game board with a player's move

    Parameters:
    - board (list): The current game board.
    - move (int): The move chosen by the player (1 to 9).
    - mark (str): The player's symbol ('X' or 'O') to be placed on the board.

    Returns:
    - None. The function updates the board in-place.
    '''

    # Calculates the corresponding row and
    column indices for the move
    row, col = divmod(move - 1, 3)
    # Updates the board with the player's mark.
    board[row][col] = mark


