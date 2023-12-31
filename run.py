import random
import os

ANSI_RED = '\u001b[31m'
ANSI_GREEN = '\u001b[32m'
ANSI_RESET = '\u001b[0m'

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

def how_to_play():
    '''
    Step by stpe on how to become a Tic Tac Toe legend:"
    '''
    print('Welcome to the ultimate Tic Tac Toe showdown!')
    print()
    print('Picture this: you\'re about to step onto a 3x3 grid, just like the one below.')
    print('Each cell is tagged with a number from 1 to 9.')
    print()
    draw_board()
    print()

    print("Guess what? You're the 'X' player, and your mission is simple:")
    print("get three 'X's in a row, column, or diagonal.")
    print("To make your move, type the number of the cell where you want to drop your 'X'.")
    print()

    print("But there's a twist – no crossing into 'O' territory, and no numbers outside of 1 to 9 allowed!")
    print()

    print("Meet your rival, the 'O' bot. It's got a few tricks up its sleeve, making random yet cunning moves.")
    print("Don't underestimate it; this bot knows how to play the game.")
    print()

    print("The first to conquer three 'X's in a row, column, or diagonal is the champion.")
    print("If all cells are claimed, and no one clinches victory, it's a draw.")

    print('You can\'t place your "X" where your opponent has already marked an "O,"')
    print('and you can\'t pick a number outside of 1 to 9.')
    print('\n')

    print('Your opponent, the bot, is the "O" player. It\'ll make its moves randomly,')
    print('but don\'t be fooled; it\'s a smart bot and won\'t step on your "X" territory.')
    print('\n')

    print('The first player to get three "X"s in a row, column, or diagonal wins.')
    print('If all the cells are filled, and no one wins, it\'s a draw.')
    print()

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
                print(ANSI_GREEN + cell + ANSI_RESET, end=' ')
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
            print(ANSI_RED + f'Oops, that\'s not a valid move. Try again, champ!' + ANSI_RESET)
            continue

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
        print(ANSI_RED + f'{move}\'s out of range, champ. Pick a number from 1 to 9.' + ANSI_RESET)
        return False
    row, col = divmod(move - 1, 3)
    # Checks if position is not already tanken
    if board[row][col] in ['X', 'O']:
        # Print error message
        print(ANSI_RED + f"Oops, that spot's taken, buddy!" + ANSI_RESET)
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
    '''
    Snag the game-winning moves!
    '''
    # Initialize an empty list to store those triumphant moves
    winning_moves = []

    for combination in winning_combinations:
        if all(board[row][col] == 'X' for row, col in combination):
            # You nailed it! Add those winning moves to the list
            winning_moves.extend(combination)
        elif all(board[row][col] == 'O' for row, col in combination):
            # It's the bot's turn to shine! Add its winning moves to the list
            winning_moves.extend(combination)  
    # Let's show those moves that brought the victory
    return winning_moves   

def play_again():
    '''
    See if user's up for a rematch
    '''
    while True:
        choice = input('Ready to dive back into the action? Wanna give it another go? (yes/no): ').strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print('C\'mon, you gotta type "yes" or "no". Give it another shot!')

def clear_screen():
    '''
    Wiping the slate clean! Let's clear the terminal screen for a fresh start.
    '''
    # If on Unix/Linux/MacOS system
    if os.name == 'posix':  
        os.system('clear')
    else:
        # On Windows
        os.system('cls')  

def main():
    '''
    It orchestrates the epic Tic Tac Toe showdown. 
    It guides the user through the game, manages the rounds, checks for a winner or a draw, 
    and offers the option to play again or bid farewell.
    '''
    # Show the user how to play this epic game
    how_to_play()
     # Get ready to start the adventure!
    input('Press "Enter" to embark on this epic journey, champs!')
    clear_screen()

    while True:
        # Here's your empty battlefield to start the showdown
        board = [[' ' for _ in range(3)] for _ in range(3)]
        # Clear the screen to create a clean slate for the battlefiel
        clear_screen()
        # Here's your empty battlefield to start the showdown
        draw_board()
        # Let the battle commence!
        round = 1

        # The showdown has 9 rounds 
        while round < 10:
            if round % 2 != 0:
                # It's your turn to shine
                board = get_user_next_move(board)
            else:
                # Now the bot makes its move
                board = get_bot_next_move(board)

            clear_screen()
            # Display the updated battlefield
            draw_board(board)

            if round > 4:
                # Time to see if there's a winner
                winner = get_winner(board)
                if winner:
                    clear_screen()
                    # Highlight winning moves
                    draw_board(board, get_winner_moves(board))
                    # Announce the champion!
                    print(f'And the undisputed champion is... {winner}!')
                    break
            # It's no fun when it loops forever
            round += 1

        if round > 9:
            # When all's said and done, if there's no winner, it's a draw!
            print("It's a tie!")

        if not play_again():
            print('Hats off to you, brave warriors! Farewell, for now.')
            break


if __name__ == '__main__':
    main()