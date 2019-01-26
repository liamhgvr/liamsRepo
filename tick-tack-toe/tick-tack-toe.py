# Tick Tack Toe

# Configuration
EXIT = 'q'
BOX = '_'

WIN = 3
MAX_USERS = 5
MAX_SIZE = 10

players_signs = ['O', 'X', 'Z', 'L', 'G']
players = {}

DEF_USERS = 2
DEF_SIZE = 3

GO_RIGHT = {'r': 0, 'c': 1}
GO_DOWN_RIGHT = {'r': 1, 'c': 1}
GO_DOWN_LEFT = {'r': 1, 'c': -1}
GO_DOWN = {'r': 1, 'c': 0}

ways = {
    'R': GO_RIGHT,
    'DR': GO_DOWN_RIGHT,
    'DL': GO_DOWN_LEFT,
    'D': GO_DOWN,
}


# Methods

def cls():
    # Clear screen
    print(chr(27) + "[2J")


def build_board():

    board_size = raw_input("==> Change board size (3 - 10): ")

    if board_size == '' or MAX_SIZE < int(board_size) < 0:
        board_size = DEF_SIZE

    new_main_board = [[BOX for x in range(int(board_size))] for y in range(int(board_size))]
    return new_main_board


def print_board(board):
    # print the game board
    row_count = 0

    for print_row in board:
        # print row number
        print bcolors.OKBLUE + "%s :" % row_count,
        row_count = row_count+1

        # print row values
        for box_index in range(len(print_row)):
            if box_index == len(print_row)-1:
                print bcolors.OKBLUE + print_row[box_index]
            else:
                print bcolors.OKBLUE + print_row[box_index],


def get_player_num():
    players_count = raw_input("==> Change players count (2 - 5): ")

    if players_count == '' or MAX_SIZE < int(players_count) < 0:
        players_count = DEF_USERS

    return players_count


def init_players():
    # Initiate players info
    num_of_users = get_player_num()

    for i in range(int(num_of_users)):
        players[players_signs[i]] = raw_input("==> Enter player name: ")

    # Print players
    print "Players:"
    for player in players:
        print players.get(player)


def get_box_index():
    # Get index from user
    print u"Enter row number first \u2193, and then column number \u2192"
    raw_user_index = raw_input("==> Choose box: ")

    while raw_user_index == '':
        raw_user_index = raw_input("==> Choose box: ")

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
        print "Box not empty! - Lost your turn!"
 

def is_tie(board):
    def_in_row = [] * len(board)
    for row in board:
        if BOX in row:
            def_in_row.append(True)
    return len(def_in_row) == 0


def is_strick(board, r, c, sign, way_to_go):

    board_limit = len(board)-1
    strike = 1

    while board[r][c] == sign and r + ways[way_to_go]['r'] <= board_limit and board_limit >= c + ways[way_to_go]['c'] >= 0:

        r = r + ways[way_to_go]['r']
        c = c + ways[way_to_go]['c']

        if board[r][c] == sign:
            strike = strike + 1

        if strike == WIN:
            return True
    return False


def is_win(board, curr_sign):

    board_limit = len(board)-1

    for row in range(board_limit):
        for col in range(board_limit):
            if board[row][col] == curr_sign:
                # Check R
                if is_strick(board, row, col, curr_sign, 'R'):
                    print "Win right"
                    return True
                # Check DR
                elif is_strick(board, row, col, curr_sign, 'DR'):
                    print "Win down right"
                    return True
                # Check DL
                elif is_strick(board, row, col, curr_sign, 'DL'):
                    print "Win down left"
                    return True
                # Check D
                elif is_strick(board, row, col, curr_sign, 'D'):
                    print "Win down"
                    return True
    return False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def play_game():

    print "####################"
    print "Hello Liam!"
    print "####################"

    to_exit = False
    init_players()
    main_board = build_board()

    cls()

    while to_exit is not True:

        cls()
        print bcolors.OKBLUE + "========================="

        for curr_sign, curr_player in players.iteritems():

            # print board
            print bcolors.OKBLUE + "Player: ", curr_player
            print bcolors.OKBLUE + "Current board:"
            print_board(main_board)

            # Game move:
            curr_index = get_box_index()

            if curr_index == EXIT or to_exit:
                print "Bye..."
                to_exit = True
                break
            else:
                change_box_value(main_board, curr_index, curr_sign)

                # TODO: condition fails
                # Check for win
                if is_win(main_board, curr_sign):
                    cls()
                    print bcolors.BOLD + "Player: " + curr_player + " won!"
                    print_board(main_board)
                    to_exit = True
                    break
                # Check for tie
                elif is_tie(main_board):
                    cls()
                    print bcolors.BOLD + "It's a tie!"
                    print_board(main_board)
                    to_exit = True
                    break


if __name__ == '__main__':
    play_game()
