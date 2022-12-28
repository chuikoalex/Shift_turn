import pygame
import numpy

import settings


class Game:
    matrices = {'tiles-3*3_color-2_variant-1': [[1, 1, 1],
                                                [1, 0, 2],
                                                [2, 2, 2]],
                'tiles-3*3_color-2_variant-2': [[1, 1, 2],
                                                [1, 0, 2],
                                                [1, 2, 2]],
                'tiles-3*3_color-3_variant-1': [[1, 1, 1],
                                                [2, 2, 2],
                                                [3, 3, 3]],
                'tiles-3*3_color-3_variant-2': [[1, 2, 3],
                                                [1, 2, 3],
                                                [1, 2, 3]],
                'tiles-3*3_color-4_variant-1': [[1, 1, 4],
                                                [2, 0, 4],
                                                [2, 3, 3]],
                'tiles-3*3_color-4_variant-2': [[1, 4, 4],
                                                [1, 0, 3],
                                                [2, 2, 3]]
                }
    colors = ['grey', 'blue', 'green', 'red', 'yellow']

    def __init__(self):
        self.GAME = False
        self.matrix_size = 3
        self.color_number = 2
        self.level = 1
        self.game_matrix = [[0] * self.matrix_size for _ in range(self.matrix_size)]

    def game_preparation(self, matrix_size=3, color_number=2, level=1):
        pass

    def run(self):
        self.GAME = True

    def status(self):
        return self.GAME
