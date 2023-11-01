import random



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



def get_user_next_move():
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
                return (next_move, 'X')
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

def get_bot_next_move():
    '''
    Generates random moves for the bot within the range of 1 to 9. It ensures
    that the chosen position on the board is not already occupied by 'X' or 'O'.

    Returns:
    - Tuple[int, str]: The bot's valid move represented as (move, 'O').
    '''
    while True:
        bot_next_move = random.randint(1, 9)
        # Calculate the row and column indices based on the random move
        row, col = divmod(bot_next_move - 1, 3)
        # Check if the board position is not 'X' or 'O' (i.e., unoccupied)
        if board[row][col] not in ['X', 'O']:
            # Return the bot's valid move
            return (bot_next_move, 'O')



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
    row, col = divmod(move - 1, 3)
    # Updates the board with the player's mark.
    board[row][col] = mark


print("Hey there, welcome to my Tic Tac Toe showdown")

# Draw the initial board
draw_board()

round = 1
while round < 10: 
    # Get user to input next move
    (move, mark) = get_next_move() if round % 2 != 0 else get_bot_next_move()

    # Update board
    update_board(board, move, mark)

    # Display the board
    draw_board()

    round += 1 
