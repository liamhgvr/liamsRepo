from random import randint
import copy

import time

BOOL_TO_NUM = {True: 1, False: 0}
LIVING = 1
DEAD = 0


class Game(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.table = map(lambda row: map(lambda col: randint(0, 1), range(self.columns)), range(self.rows))

    def _find_living_neighbors(self, table, x, y):
        index_list = self._get_index_list_to_iterate(x, y)
        return sum(map(lambda index_tuple: table[index_tuple[0]][index_tuple[1]], index_list))

    def _get_index_list_to_iterate(self, x, y):
        index_list = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                      (x, y + 1), (x + 1, y + 1)]
        valid_index_list = filter(lambda index_tuple:
                                  0 <= index_tuple[0] < self.rows and 0 <= index_tuple[1] < self.columns, index_list)
        return valid_index_list

    def cycle(self):
        temp_table = copy.deepcopy(self.table)
        map(lambda i: self._handle_cell(temp_table, i / self.rows, i % self.columns), range(self.rows * self.columns))

    def _handle_cell(self, temp_table, x, y):
        neighbors_alive = self._find_living_neighbors(temp_table, x, y)
        self._define_cell_new_state(neighbors_alive, x, y)

    def _define_cell_new_state(self, neighbors_alive, x, y):
        dict_to_func = {LIVING: self._decide_for_living,
                        DEAD: self._decide_for_dead}
        self.table[x][y] = BOOL_TO_NUM[dict_to_func[self.table[x][y]](neighbors_alive)]

    @staticmethod
    def _decide_for_living(neighbors_alive):
        return neighbors_alive < 2 or neighbors_alive > 3

    @staticmethod
    def _decide_for_dead(neighbors_alive):
        return neighbors_alive == 3

    def print_table(self):
        rows = map(lambda row: self.table[row], range(self.rows))
        map(self._print_row, rows)

    @staticmethod
    def _print_row(row):
        print(row)


if __name__ == '__main__':
    game = Game(10, 10)
    game.print_table()
    while True:
        print("cycle")
        game.cycle()
        game.print_table()
        time.sleep(1)
