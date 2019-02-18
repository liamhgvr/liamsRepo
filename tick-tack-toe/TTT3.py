# Multi Player Tick Tack Toe


DEF_CELL_VALUE = '_'
DEF_SIZE = 3
MAX_SIZE = 5
DEF_MIN_PLAYERS = 2
players = {}


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


class Cell:

    def __init__(self, value=DEF_CELL_VALUE):
        self.value = value

    def change_cell_value(self, new_value):
        self.value = new_value

    def is_free_cell(self):
        return self.value == DEF_CELL_VALUE


class Board:

    def __init__(self, size=DEF_SIZE):
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
            print "Turn lost"


if __name__ == '__main__':

    b = Board()
    b.print_board()
    b.select_cell(2, 0, 'S')
    b.select_cell(2, 1, 'X')
    b.select_cell(2, 2, '0')
    b.select_cell(2, 2, 'E')
    b.print_board()

    p = Players()
    p.get_players()
