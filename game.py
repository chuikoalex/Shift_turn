import numpy

from random import randint, shuffle

import settings


class Game:
    matrices = {'2-color-quantity-var': 2,
                '3-color-quantity-var': 2,
                '4-color-quantity-var': 2,
                'tiles-3*3_color-2_var-1': [['blue', 'blue', 'blue'],
                                            ['blue', 0, 'green'],
                                            ['green', 'green', 'green']],
                'tiles-3*3_color-2_var-2': [['blue', 'blue', 'green'],
                                            ['blue', 0, 'green'],
                                            ['blue', 'green', 'green']],
                'tiles-3*3_color-3_var-1': [['blue', 'blue', 'blue'],
                                            ['green', 'green', 'green'],
                                            ['red', 'red', 'red']],
                'tiles-3*3_color-3_var-2': [['blue', 'green', 'red'],
                                            ['blue', 'green', 'red'],
                                            ['blue', 'green', 'red']],
                'tiles-3*3_color-4_var-1': [['blue', 'blue', 'yellow'],
                                            ['green', 0, 'yellow'],
                                            ['green', 'red', 'red']],
                'tiles-3*3_color-4_var-2': [['blue', 'yellow', 'yellow'],
                                            ['blue', 0, 'red'],
                                            ['green', 'green', 'red']]
                }

    def __init__(self):
        self.RUN_GAME = False
        self.matrix_size = 3
        self.color_number = 2
        self.level = 1
        self.step = 0

        self.game_start_matrix = self.create_start_matrix()
        self.np_matrix_start = numpy.array(self.game_start_matrix)
        self.np_matrix_left = numpy.array(self.game_start_matrix)
        self.np_matrix_right = numpy.array(self.game_start_matrix)

    def create_start_matrix(self):
        var = randint(1, Game.matrices[f'{self.color_number}-color-quantity-var'])
        key = f'tiles-{self.matrix_size}*{self.matrix_size}_color-{self.color_number}_var-{var}'
        matrix = [[col for col in row] for row in Game.matrices[key]]  # полная копия двумерного списка
        name_color = [v for v in settings.colors.values() if v != 'grey']
        shuffle(num_color := [k for k in settings.colors.keys() if k != 0])
        color = dict(zip(name_color, num_color))
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != 0:
                    matrix[row][col] = color[matrix[row][col]]
        return matrix

    def get_start_matrix(self):
        return self.game_start_matrix

    def set_attributes_matrix(self, matrix_size=3, color_number=2):
        self.matrix_size = matrix_size
        self.color_number = color_number
        self.stop()

    def signal_from_board(self, signal):
        ...

    def rotate_right(self):
        self.np_matrix_left = numpy.rot90(self.np_matrix_left, k=-1)
        self.np_matrix_right = numpy.rot90(self.np_matrix_right)

    def rotate_down(self):
        self.np_matrix_left = numpy.rot90(self.np_matrix_left)
        self.np_matrix_right = numpy.rot90(self.np_matrix_right, k=-1)

    def shift_right(self, row=-1):
        if row == -1:
            self.np_matrix_left = numpy.roll(self.np_matrix_left, 1)
            self.np_matrix_right = numpy.roll(self.np_matrix_right, -1)
        else:
            self.np_matrix_left[row] = numpy.roll(self.np_matrix_left[row], 1)
            self.np_matrix_right[row] = numpy.roll(self.np_matrix_right[row], -1)

    def shift_down(self, col=-1):
        if col == -1:
            self.np_matrix_left = numpy.roll(self.np_matrix_left, -1, (0, 0))
            self.np_matrix_right = numpy.roll(self.np_matrix_right, 1, (0, 0))
        else:
            self.np_matrix_left = numpy.rot90(self.np_matrix_left, k=-1)
            self.np_matrix_left[col] = numpy.roll(self.np_matrix_left[col], -1)
            self.np_matrix_left = numpy.rot90(self.np_matrix_left)
            self.np_matrix_right = numpy.rot90(self.np_matrix_right, k=-1)
            self.np_matrix_right[col] = numpy.roll(self.np_matrix_right[col], 1)
            self.np_matrix_right = numpy.rot90(self.np_matrix_right)

    def set_level(self, level=1):
        self.level = level
        self.stop()

    def run(self):
        self.RUN_GAME = True
        print('game run')

    def stop(self):
        self.RUN_GAME = False
        self.game_start_matrix = self.create_start_matrix()
        self.np_matrix_start = numpy.array(self.game_start_matrix)
        self.np_matrix_left = numpy.array(self.game_start_matrix)
        self.np_matrix_right = numpy.array(self.game_start_matrix)
        print('game stop')

    def is_win(self):
        start_and_left = self.np_matrix_start == self.np_matrix_left
        start_and_right = self.np_matrix_start == self.np_matrix_right
        return start_and_left.all() == start_and_right.all()

    def is_fail(self):
        if self.step == 0:
            return True
        return False

    def get_status(self):
        return self.RUN_GAME


if __name__ == '__main__':
    ...
