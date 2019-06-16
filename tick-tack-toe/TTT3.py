# Multi Player Tick Tack Toe


DEF_CELL_VALUE = '_'
DEF_BOARD_SIZE = 3
MAX_BOARD_SIZE = 5
MIN_MUN_PLAYERS = 2
MAX_MUN_PLAYERS = 5

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


class Cell:

    def __init__(self, value=DEF_CELL_VALUE):
        self.value = value

    def change_cell_value(self, new_value):
        self.value = new_value

    def is_free_cell(self):
        return self.value == DEF_CELL_VALUE


class Board:

    def __init__(self, size=DEF_BOARD_SIZE):
        self.size = size
        rows = [None] * size
        cols = rows * size

        self.board_layout = cols
        self.board_layout = [[Cell() for x in range(self.size)] for y in range(self.size)]

    def print_board(self):
        print "====================="
        for row in self.board_layout:
            for cell in row:
                print cell.value + " ",
            print "\n"

    def select_cell(self, row, col, new_value):
        if self.board_layout[row][col].is_free_cell():
            self.board_layout[row][col].change_cell_value(new_value)
        else:
            print "Lost turn"

    def get_sign_indices(self, sign_to_find):
        # Yield the locations of the given sign
        board_limit = self.size-1
        r, c = 0, 0

        while r is not board_limit and c is not board_limit:
            if self.board_layout is sign_to_find:
                yield r, c
            else:
                if c is board_limit:
                    r, c = +1, 0
                else:
                    c = +1

    def is_win(self, sign_to_check):
        board_limit = self.size-1
        win_count = self.size
        r, c = self.get_sign_indices(sign_to_check)

        return False


class Players:

    def __init__(self):
        self.players = {}
        self.players_count = 3

    def get_players_count(self):
        return self.players_count

    def get_players(self):

        players_signs = ['O', 'X', 'Z', 'A', 'G']

        for i in range(self.players_count):
            user_name = raw_input("==> Enter player name: ")
            self.players[players_signs[i]] = user_name

        # Print players
        print "Players:"
        for sign, player_name in self.players.iteritems():
            print sign, player_name

    def get_next_player(self):
        for sign, player_name in self.players.iteritems():
            yield [sign, player_name]


if __name__ == '__main__':

    b = Board()
    b.print_board()
    b.select_cell(2, 0, 'S')
    b.select_cell(2, 1, 'S')
    b.select_cell(2, 2, 'S')
    b.select_cell(1, 2, 'E')
    b.print_board()

    # p = Players()
    # p.get_players()
