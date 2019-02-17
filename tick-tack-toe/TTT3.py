# Multi Player Tick Tack Toe


DEF_CELL_VALUE = '_'
DEF_SIZE = 3


class Cell:

    def __init__(self, value=DEF_CELL_VALUE):
        self.value = value

    def change_cell_value(self, new_value):
        self.value = new_value


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
        # TODO: add is_empty_cell
        self.board_layout[row][col].change_cell_value(new_value)


b = Board()
b.print_board()
b.select_cell(2, 1, 'X')
b.print_board()
