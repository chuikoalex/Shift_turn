import pygame
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

        self.game_start_matrix = self.create_start_matrix()
        self.np_matrix_start = numpy.array(self.game_start_matrix)
        self.np_matrix_left = numpy.array(self.game_start_matrix)
        self.np_matrix_right = numpy.array(self.game_start_matrix)

    def set_attributes_matrix(self, matrix_size=3, color_number=2):
        self.RUN_GAME = False
        self.matrix_size = matrix_size
        self.color_number = color_number
        self.game_start_matrix = self.create_start_matrix()

    def set_level(self, level=1):
        self.RUN_GAME = False
        self.level = level

    def run(self):
        self.RUN_GAME = True

    def get_status(self):
        return self.RUN_GAME

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


