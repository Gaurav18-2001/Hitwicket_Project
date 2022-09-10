import numpy as np

board=[ [ ' -  ' for i in range(5) ] for j in range(5) ]
pawn_count=[5,5]

#prints board
def print_board(board):
    for r in board:
        for c in r:
            print(c,end = "      ")
        print()

#take input
def define_pawn_names():
    A_pawn_names=input('Player1 Input: ').split(', ')
    A_pawn_names=['B-'+ s for s in A_pawn_names]
    board[0]=A_pawn_names
    B_pawn_names=input('Player2 Input: ').split(', ')
    B_pawn_names=['A-'+ s for s in B_pawn_names]
    board[4]=B_pawn_names

#returns location of pawn
def locate(player,pawn_name,board):
    np_board = np.array(board)
    location = np.argwhere(np_board == player + '-' + pawn_name)
    return location

#move and delete pawns
def move_character(player,move_details):
    [[m,l]]=locate(player,move_details[0],board)
    if move_details[1]=='F':
        if player == 'A':
            if board[m-1][l] != ' -  ':
                pawn_count[1]-=1
                board[m-1][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-1][l] = board[m][l]
                print_board(board)
                board[m][l] = ' -  '
        if player == 'B':
            if board[m+1][l] != ' -  ':
                pawn_count[0]-=1
                board[m+1][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+1][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='B':
        if player == 'A':
            if board[m+1][l] != ' -  ':
                pawn_count[1]-=1
                board[m+1][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+1][l] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m-1][l] != ' -  ':
                pawn_count[0]-=1
                board[m-1][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-1][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='L':
        if player == 'A':
            if board[m][l-1] != ' -  ':
                pawn_count[1]-=1
                board[m][l-1] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-1] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l+1] != ' -  ':
                pawn_count[0]-=1
                board[m][l+1] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+1] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='R':
        if player == 'A':
            if board[m][l+1] != ' -  ':
                pawn_count[1]-=1
                board[m][l+1] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+1] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l-1] != ' -  ':
                pawn_count[0]-=1
                board[m][l-1] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-1] = board[m][l]
                board[m][l] = ' -  '
    print_board(board)

def move_h1(player,move_details):
    [[m,l]]=locate(player,move_details[0],board)
    if move_details[1]=='FL':
        if player == 'A':
            if board[m-2][l] != ' -  ':
                pawn_count[1]-=1
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-2][l] = board[m][l]
                print_board(board)
                board[m][l] = ' -  '
        if player == 'B':
            if board[m+2][l] != ' -  ':
                pawn_count[0]-=1
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='FR':
        if player == 'A':
            if board[m+2][l] != ' -  ':
                pawn_count[2]-=1
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m-2][l] != ' -  ':
                pawn_count[0]-=1
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='BL':
        if player == 'A':
            if board[m][l-2] != ' -  ':
                pawn_count[2]-=1
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l+2] != ' -  ':
                pawn_count[0]-=1
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='BR':
        if player == 'A':
            if board[m][l+2] != ' -  ':
                pawn_count[2]-=1
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l-2] != ' -  ':
                pawn_count[0]-=1
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '

def move_h2(player,move_details):
    [[m,l]]=locate(player,move_details[0],board)
    if move_details[1]=='F':
        if player == 'A':
            if board[m-2][l] != ' -  ':
                pawn_count[1]-=1
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-2][l] = board[m][l]
                print_board(board)
                board[m][l] = ' -  '
        if player == 'B':
            if board[m+2][l] != ' -  ':
                pawn_count[0]-=1
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='B':
        if player == 'A':
            if board[m+2][l] != ' -  ':
                pawn_count[2]-=1
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m-2][l] != ' -  ':
                pawn_count[0]-=1
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='L':
        if player == 'A':
            if board[m][l-2] != ' -  ':
                pawn_count[2]-=1
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l+2] != ' -  ':
                pawn_count[0]-=1
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='R':
        if player == 'A':
            if board[m][l+2] != ' -  ':
                pawn_count[2]-=1
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l+2] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m][l-2] != ' -  ':
                pawn_count[0]-=1
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m][l-2] = board[m][l]
                board[m][l] = ' -  '
    elif move_details[1]=='B':
        if player == 'A':
            if board[m+2][l] != ' -  ':
                pawn_count[2]-=1
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m+2][l] = board[m][l]
                board[m][l] = ' -  '
        if player == 'B':
            if board[m-2][l] != ' -  ':
                pawn_count[0]-=1
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '
            else:
                board[m-2][l] = board[m][l]
                board[m][l] = ' -  '

def move(player):
    move_details = input('Player ' + player +'\'s Move: ').split(':')
    if move_details[0] == 'H1':
        move_h1(player)
    elif move_details[0] == 'H2':
        move_h2(player)
    else:
        move_character(player)

def main():
    define_pawn_names()
    print_board(board)
    while(pawn_count[0] != 0 or pawn_count[1] != 0):
        move('A')
        if(pawn_count[1] != 0):
            move('B')
    if pawn_count[0] == 0:
        print('Player B won!!')
    else:
        print('Player A won!!')

if _name_ == '_main_':
    main()
