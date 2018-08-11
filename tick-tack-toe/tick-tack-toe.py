# Tick Tack Toe

import os

# Configuration
EXIT = 'q'
DEF_BOX = '_'

players = {'X': "", 'O': ""}

def_board_size = 3

main_board = [[DEF_BOX, DEF_BOX, DEF_BOX], [DEF_BOX, DEF_BOX, DEF_BOX], [DEF_BOX, DEF_BOX, DEF_BOX]]


# Methods
def print_board(board):
    # print the game board
    for print_row in board:
        for box_index in range(len(print_row)):
            if box_index == len(print_row)-1:
                print print_row[box_index]
            else:
                print print_row[box_index],


def init_players():
    # Initiate players info
    for item in players:
        players[item] = raw_input("Enter player name: ")

    # Print players
    print "Players:"
    for player in players:
        print players.get(player)


def get_box_index():
    # Get index from user
    raw_user_index = raw_input("Choose box: ")
    if raw_user_index == EXIT:
        return raw_user_index
    else:
        user_index = list(raw_user_index)
        return user_index


def change_box_value(board, index, user_sign):
    # Change the value of box
    r = int(index[0])
    c = int(index[1])

    if board[r][c] == DEF_BOX:
        board[r][c] = user_sign
    else:
        print "Box not empty!"


def is_tie(board):
    for r in board:
        for c in r:
            if c == DEF_BOX:
                return True
            else:
                return False


def check_for_win(board, curr_user_sign):
    # Check for 3 signs in a row
    limit = len(board)-1

    for r in range(limit):
        for c in range(limit):
            if board[r][c] == curr_user_sign:
                # Check R
                if c < limit and board[r][c+1] == curr_user_sign:
                    if c < limit-1 and board[r][c+2] == curr_user_sign:
                        return True
                # Check DR
                if c < limit and r < limit and board[r+1][c+1] == curr_user_sign:
                    if c < limit-1 and r < limit-1 and board[r+2][c+2] == curr_user_sign:
                        return True
                # Check DL
                if c > 0 and r < limit and board[r+1][c-1] == curr_user_sign:
                    if c > 2 and r < limit-1 and board[r+2][c-2] == curr_user_sign:
                        return True
                # Check D
                if r < limit and board[r+1][c] == curr_user_sign:
                    if r < limit-1 and board[r+2][c] == curr_user_sign:
                        return True
                else:
                    return False


def play_game():

    print "Welcome to Hell"
    playing = True
    init_players()

    while playing:

        for curr_sign, curr_player in players.iteritems():
            print(chr(27) + "[2J")
            print "Current board:"
            print_board(main_board)

            # Game move:
            print "Player: ", curr_player
            curr_index = get_box_index()

            if curr_index == EXIT:
                print "Bye..."
            else:
                change_box_value(main_board, curr_index, curr_sign)

                # Check for winning condition
                if check_for_win(main_board, curr_sign):
                    print(chr(27) + "[2J")
                    # Winner
                    print "Player: " + curr_player + " won!"
                    print_board(main_board)
                    playing = False
                    break
                elif is_tie(main_board):
                    print(chr(27) + "[2J")
                    # Tie
                    print "It's a tie!"
                    playing = False
                    break

        if playing is False:
            break


if __name__ == '__main__':
    play_game()
