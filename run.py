import random

print("Hey there, welcome to my Tic Tac Toe showdown")

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def draw_board():
    for row in board:
        print('+---+---+---+')
        print('|', end=' ')
        print(' | '.join(row), end=' ')
        print('|')
    print('+---+---+---+')

def validate_move(move):
    if move < 1 or move > 9:
        print(f"{move}'s out of range, champ. Pick a number from 1 to 9.")
        return False
    row, col = divmod(move - 1, 3)
    if board[row][col] in ['X', 'O']:
        print("Oops, that spot's taken, buddy!")
        return False
    return True


def get_next_move():
    while True:
        try: 
            next_move = int(input("What's your move, superstar? Pick a number from 1 to 9: "))
            if validate_move(next_move):
                return next_move
        except ValueError:
            print("Oops, that's not a valid move. Try again, champ!")    


def update_board(board, move, mark):
    row, col = divmod(move - 1, 3)
    board[row][col] = mark

