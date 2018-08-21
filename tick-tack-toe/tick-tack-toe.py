# Tick Tack Toe

# Configuration
EXIT = 'q'
BOX = '_'

WIN = 3
MAX_USERS = 5
MAX_SIZE = 10

players_signs = ['X', 'O', 'Z', 'L', 'G']
players = {}

DEF_USERS = 2
DEF_SIZE = 3


ways = {
    'r': {'r': 0, 'c': 1},
    'dr': {'r': 1, 'c': 1},
    'dl': {'r': 1, 'c': -1},
    'd': {'r': 1, 'c': 0},
}


# Methods

def build_board():

    resize_to = DEF_SIZE
    user_size = int(raw_input("Change board size (3 - 10): "))

    if user_size != '' and MAX_SIZE >= user_size > 0:
        resize_to = user_size

    new_main_board = [[BOX for x in range(resize_to)] for y in range(resize_to)]
    return new_main_board


def print_board(board):
    # print the game board
    row_count = 0

    for print_row in board:
        # print row numer
        print "%s :" % row_count,
        row_count = row_count+1

        # print row values
        for box_index in range(len(print_row)):
            if box_index == len(print_row)-1:
                print print_row[box_index]
            else:
                print print_row[box_index],


def get_player_num():
    new_players_count = raw_input("Change players count (2 - 5): ")

    if new_players_count != '' and MAX_SIZE >= int(new_players_count) > 0:
        return new_players_count
    else:
        return DEF_USERS


def init_players():
    # Initiate players info
    num_of_users = get_player_num()

    for i in range(int(num_of_users)):
        players[players_signs[i]] = raw_input("Enter player name: ")

    # Print players
    print "Players:"
    for player in players:
        print players.get(player)


def get_box_index():
    # Get index from user
    print u"Enter row number first \u2193, and then column number \u2192"
    raw_user_index = raw_input("Choose box: ")

    while raw_user_index == '':
        raw_user_index = raw_input("Choose box: ")

    if raw_user_index == EXIT:
        return raw_user_index
    else:
        user_index = list(raw_user_index)
        return user_index


def change_box_value(board, index, user_sign):
    # Change the value of box
    board_size = len(board)-1
    r = int(index[0])
    c = int(index[1])

    if board[r][c] == BOX:
        board[r][c] = user_sign
    elif board_size < board[r][c] or 0 > board[r][c]:
        print "Bad input - Lost your turn!"
    else:
        print "Box not empty!"


def is_tie(board):
    def_in_row = [] * len(board)
    for row in board:
        if BOX in row:
            def_in_row.append(True)
    return len(def_in_row) == 0


def is_strick(board, r, c, sign, way_to_go):

    board_limit = len(board)-1
    strike = WIN-1

    while (r + ways[way_to_go]['r']) + (c + ways[way_to_go]['c']) <= board_limit and c + ways[way_to_go]['c'] >= 0:

        r = r + ways[way_to_go]['r']
        c = c + ways[way_to_go]['c']

        if board[r][c] == sign:
            strike = strike - 1

            if strike == 0:
                return True
    return False


def is_win(board, curr_sign):

    board_limit = len(board)-1

    for row in range(board_limit):
        for col in range(board_limit):
            if board[row][col] == curr_sign:
                # Check R
                if is_strick(board, row, col, curr_sign, 'r'):
                    print "Win right"
                    return True
                # Check DR
                elif is_strick(board, row, col, curr_sign, 'dr'):
                    print "Win down right"
                    return True
                # Check DL
                elif is_strick(board, row, col, curr_sign, 'dl'):
                    print "Win down left"
                    return True
                # Check D
                elif is_strick(board, row, col, curr_sign, 'd'):
                    print "Win down"
                    return True
    return False


def play_game():

    print "Welcome to Hell"

    to_exit = False
    init_players()
    main_board = build_board()

    print(chr(27) + "[2J")

    while to_exit:
        print(chr(27) + "[2J")
        print "==============="
        for curr_sign, curr_player in players.iteritems():
            print "Current board:"
            print_board(main_board)

            # Game move:
            print "Player: ", curr_player
            curr_index = get_box_index()

            if curr_index == EXIT or to_exit:
                print "Bye..."
                break
            else:
                change_box_value(main_board, curr_index, curr_sign)

                # Check for winning condition
                if is_win(main_board, curr_sign):
                    print(chr(27) + "[2J")
                    # Winner
                    print "Player: " + curr_player + " won!"
                    print_board(main_board)
                    to_exit = True
                elif is_tie(main_board):
                    # Tie
                    print(chr(27) + "[2J")
                    print "It's a tie!"
                    print_board(main_board)
                    to_exit = True


if __name__ == '__main__':
    play_game()
