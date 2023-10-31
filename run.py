import random

print('Hey there, welcome to my Tic Tac Toe showdown')

moves = list(range(1, 10))
board = [list(range(1, 4)), list(range(4, 7)), list(range(7, 10))]

def draw_board():
    '''
    The `draw_board` function iterates through the Tic Tac Toe board, 
    printing a visual representation by adding borders and values from the `board` list.
    '''
    # Loop through each row of the board (3 rows in total)
    for row in range(3):
        # Print the top border of the row
        print('\n+---+---+---+')
        # Print the content of the row
        print('|', end = '')
        for col in range(3):
            # Print the value from the board for the current position
            print('', board[row][col], end = ' |')
     # Print the bottom border of the row
    print('\n+---+---+---+')

draw_board()