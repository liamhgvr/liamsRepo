# Tick Tack Toe

# Configuration
EXIT = 'q'
DEF_BOX = '_'

MAX_USERS = 5
MAX_SIZE = 10

players_signs = ['X', 'O', 'Z', 'L', 'G']
players = {}

DEF_USERS = 2
DEF_SIZE = 3

board_size = DEF_SIZE

main_board = []


# Methods
def build_board():
    new_board_size = raw_input("Change board size (3 - 10): ")

    if new_board_size != '' and MAX_SIZE >= int(new_board_size) > 0:
        new_main_board = [[DEF_BOX for x in range(int(new_board_size))] for y in range(int(new_board_size))]
        return new_main_board
    else:
        def_main_board = [[DEF_BOX for x in range(DEF_SIZE)] for y in range(DEF_SIZE)]
        return def_main_board


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
    r = int(index[0])
    c = int(index[1])

    if board[r][c] == DEF_BOX:
        board[r][c] = user_sign
    elif board_size < board[r][c] or 0 > board[r][c]:
        print "Bad input - Lost your turn!"
    else:
        print "Box not empty!"


def is_tie(board):
    def_in_row = [] * len(board)
    for row in board:
        if DEF_BOX in row:
            def_in_row.append(True)
    return len(def_in_row) == 0


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
                    if c+1 < limit-1 and r+1 < limit-1 and board[r+2][c+2] == curr_user_sign:
                        return True
                # Check DL
                if c > 0 and r < limit and board[r+1][c-1] == curr_user_sign:
                    if c-1 > 0 and r+1 < limit-1 and board[r+2][c-2] == curr_user_sign:
                        return True
                # Check D
                if r < limit and board[r+1][c] == curr_user_sign:
                    if r+1 < limit-1 and board[r+2][c] == curr_user_sign:
                        return True
                else:
                    return False


def play_game():

    print "Welcome to Hell"

    playing = True
    init_players()
    main_board = build_board()

    print(chr(27) + "[2J")

    while playing:
	print(chr(27) + "[2J")
        print "==============="
        for curr_sign, curr_player in players.iteritems():
            print "Current board:"
            print_board(main_board)

            # Game move:
            print "Player: ", curr_player
            curr_index = get_box_index()

            if curr_index == EXIT:
                print "Bye..."
                playing = False
                break
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
                    # Tie
		    print(chr(27) + "[2J")
                    print "It's a tie!"
                    print_board(main_board)
                    playing = False
                    break

        if playing is False:
            break


if __name__ == '__main__':
    play_game()
