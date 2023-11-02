import random
from colorama import Fore, Style

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],  # Top row
    [(1, 0), (1, 1), (1, 2)],  # Middle row
    [(2, 0), (2, 1), (2, 2)],  # Bottom row
    [(0, 0), (1, 0), (2, 0)],  # Left column
    [(0, 1), (1, 1), (2, 1)],  # Middle column
    [(0, 2), (1, 2), (2, 2)],  # Right column
    [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
    [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
]

def draw_board(board=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], winning_moves=None):
    '''
    Show off the Tic Tac Toe board in all its glory, complete with borders and battle marks.
    '''
    # Loop through each row of the game board
    for row_index, row in enumerate(board):
        print('+---+---+---+')
        # Print the content of the row, joining values with ' | '
        print('|', end=' ')
        for col_index, cell in enumerate(row):
            if (winning_moves is not None) and ((row_index, col_index) in winning_moves):
                print(f"{Fore.GREEN}{cell}{Style.RESET_ALL}", end=' ')
            else:
                print(cell, end=' ')
            if col_index < 2:
                print('|', end=' ')
        # End the row with a border and a new line
        print('|')
    # Print the bottom border of the board to complete the visual representation
    print('+---+---+---+')


def get_user_next_move(board):
    '''
    Get user to input next move by typing a number from 1 to 9. 
    It's not going to let you move to a spot that's already been claimed.
    '''

    ## Time to play, superstar! We're in an endless loop until you make a killer move.
    while True:
        try: 
            # Get your move by entering a number from 1 to 9. We'll check if it's the real deal.
            next_move = int(input("What's your move, superstar? Pick a number from 1 to 9: "))
            if validate_move(next_move, board):
                # If your move checks out, it's showtime. Your 'X' is dropping right here!
                move, mark = (next_move, 'X')
                board = update_board(board, move, mark)
                # Handing you back the updated board.
                return board
        except ValueError:
            # Oops! If you stumble with non-numeric input, we'll tell you off in red.
            print(f"{Fore.RED}Oops, that's not a valid move. Try again, champ!{Style.RESET_ALL}")


def get_bot_next_move(board):
    '''
    The bot's turn to shine with a random, clever move. 
    It avoids crossing your 'X' or 'O' territory.
    '''
    while True:
        bot_next_move = random.randint(1, 9)
        # Calculate the row and column indices based on the random move
        row, col = divmod(bot_next_move - 1, 3)
        # Make sure the spot isn't already occupied by 'X' or 'O'
        if board[row][col] not in ['X', 'O']:
            move, mark = (bot_next_move, 'O')
            board = update_board(board, move, mark)
            return board


def validate_move(move, board):
    '''
    Make sure that move of yours is the real deal for this Tic Tac Toe showdown.    
    '''
    if move < 1 or move > 9:
        # Print out-of-range moves
        print(f'{move}\'s out of range, champ. Pick a number from 1 to 9.')
        return False
    row, col = divmod(move - 1, 3)
    # Checks if position is not already tanken
    if board[row][col] in ['X', 'O']:
        # Print error message
        print(f"{Fore.RED}Oops, that spot's taken, buddy!{Style.RESET_ALL}")
        return False
    return True


def update_board(board, move, mark):
    '''
    Drop your mark on the Tic Tac game board
    '''

    # Figure out where your mark lands and then BAM!
    row, col = divmod(move - 1, 3)
    #  The board's got your mark
    board[row][col] = mark
    return board


def get_winner(board):
    '''
    Get the champ of the Tic Tac Toe showdown by scanning all the possible ways you can win - 
    whether it's three in a row, column, or even diagonally.
    '''
    # See if anyone aced a row,
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # nailed a column, 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # or slayed it diagonally to become the champ
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
        
    # If there ain't no champ to be found...
    return None  


def get_winner_moves(board):
    winning_moves = []  # Initialize an empty list to store winning moves

    for combination in winning_combinations:
        if all(board[row][col] == 'X' for row, col in combination):
            winning_moves.extend(combination)  # Add winning moves to the list
        elif all(board[row][col] == 'O' for row, col in combination):
            winning_moves.extend(combination)  # Add winning moves to the list

    return winning_moves  # Return the list of winning moves


def play_again():
    while True:
        choice = input('Ready for another round? Want to play again? (yes/no): ').strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print('C\'mon, you gotta type "yes" or "no". Give it another shot!')


def main():
    print("Hey there, welcome to my Tic Tac Toe showdown")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]

    draw_board()

    round = 1
    while round < 10: 
        if round % 2 != 0:
            board = get_user_next_move(board)
        else:
            board = get_bot_next_move(board)

        if round > 4:
            winner = get_winner(board)
            if winner:
                
                draw_board(board, get_winner_moves(board))
                print(f'The winner is {winner}!')
                break

        draw_board(board)
        round += 1

    if round > 9: 
        print("It's a draw!")

main()