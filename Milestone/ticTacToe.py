### Tic Tac Toe ###
### Milestone Project by Chris Ford ###


import random

##Define a play board
def display_board(board):
    print('\n'*100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

##Test Board to test functions and sets
##test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O','X']

##Determine which marker player wants to user, X or O
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return ('O', 'X')


##Define where the marker will be placed on the board
def place_marker(board, marker, position):
    board[position] = marker

##Testing place_marker(board, marker, position)
#place_marker(test_board, '$', 8)
#display_board(test_board)

##Function to see if anyone has won the game
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #Across top
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Across middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or #Across bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or #Down middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or #Down middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or #Down right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or #Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #Diagonal

#win_check(test_board, 'X')

##Random module to determine which player goes first
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

##Function to determine if there is space for another marker in a specified space
def space_check(board, position):
    return board[position] == ' '

##Function to determine if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

##Function to ask for player's move, positon 1 - 9, checking to see if position is available
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(turn + ', please choose your next position: (1 - 9)    '))

    return position

##Function to see if user wants to play again
def replay():
    return input('Do you want to play again? Enter Yes or No. ').lower().startswith('y')


##Running the game
print('Welcome to Tic Tac Toe! ')

while True:
    #Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No. ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Player 1's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 wins the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is  draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #Player 2's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 wins the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is  draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
