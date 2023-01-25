import numpy
from random import randint, shuffle, choice

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
        self.stars = 0

        self.game_start_matrix = self.create_start_matrix()
        self.np_matrix_start = numpy.array(self.game_start_matrix)
        self.np_matrix_left = numpy.array(self.game_start_matrix)
        self.np_matrix_right = numpy.array(self.game_start_matrix)

    def create_start_matrix(self):
        """Функция создает стартовую матрицу для игры.
           Берем шаблон и случайным образом заменяем полученное расположение цветом.
           Таблица с вариантами цветов берется из 'setting' """

        var = randint(1, Game.matrices[f'{self.color_number}-color-quantity-var'])
        key = f'tiles-{self.matrix_size}*{self.matrix_size}_color-{self.color_number}_var-{var}'
        matrix = [[col for col in row] for row in Game.matrices[key]]  # полная копия двумерного списка
        name_color = [color for color in settings.colors.values() if color != 'grey']
        shuffle(num_color := [k for k in settings.colors.keys() if k != 0])
        color = dict(zip(name_color, num_color))
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != 0:
                    matrix[row][col] = color[matrix[row][col]]
        return matrix

    def create_matrices(self):
        """Функция строит Numpy матрицы на основе стартовой.
        Для отображения тайлов np_matrix_left и np_matrix_right.
        Для хранения необходимой сборки np_matrix_start."""

        self.game_start_matrix = self.create_start_matrix()
        self.np_matrix_start = numpy.array(self.game_start_matrix)
        self.np_matrix_left = numpy.array(self.game_start_matrix)
        self.np_matrix_right = numpy.array(self.game_start_matrix)

    def set_attributes_matrix(self, matrix_size=3, color_number=2):
        self.matrix_size = matrix_size
        self.color_number = color_number
        self.create_matrices()

    def set_level(self, level=1):
        self.level = level
        self.create_matrices()

    def signal_from_board(self, signal: str, line: int):
        """Функция обработки сигнала полученного от нажатия кнопки сдвига тайлов."""

        self.step -= 1

        if signal.startswith("rotate"):
            eval(f"self.{signal}()")
        elif signal.startswith("shift_right"):
            eval(f"self.shift_right({line})")
        elif signal.startswith("shift_down"):
            eval(f"self.shift_down({line})")

        if self.is_win():
            self.stop()
            return 'win'

        if self.is_fail():
            self.stop()
            return 'fail'

    def get_matrix_left(self):
        return self.np_matrix_left

    def get_matrix_right(self):
        return self.np_matrix_right

    # Четыре функции трансформации массивов для отображения тайлов
    def rotate_right(self):
        self.np_matrix_left = numpy.rot90(self.np_matrix_left, k=-1)
        self.np_matrix_right = numpy.rot90(self.np_matrix_right)

    def rotate_down(self):
        self.np_matrix_left = numpy.rot90(self.np_matrix_left)
        self.np_matrix_right = numpy.rot90(self.np_matrix_right, k=-1)

    def shift_right(self, row=-1):
        if row == -1:
            self.np_matrix_left = numpy.rot90(self.np_matrix_left, k=-1)
            self.np_matrix_left = numpy.roll(self.np_matrix_left, -1, (0, 0))
            self.np_matrix_left = numpy.rot90(self.np_matrix_left)
            self.np_matrix_right = numpy.rot90(self.np_matrix_right, k=-1)
            self.np_matrix_right = numpy.roll(self.np_matrix_right, 1, (0, 0))
            self.np_matrix_right = numpy.rot90(self.np_matrix_right)
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
    # ----------------------------------------------------------------------------

    def run(self):
        """Функция запуска игры
         (количество ходов - 10, количество возможных звезд - 3).
         Вызываем замешивание матриц (np_matrix_left и np_matrix_right)."""

        self.RUN_GAME = True
        self.step = 10
        self.stars = 3
        self.intermix_matrix()

    def intermix_matrix(self):
        commands = {"rotate_right": (2, 4),
                    "shift_right_long": (0, 3),
                    "shift_right_short": (0, 3),
                    "shift_down_short": (0, 3),
                    "shift_down_long": (0, 3),
                    "rotate_down": (0.5, 4)}

        mix = self.level * 5
        previous_command = ""
        repeat_command = 0
        while mix > 0:
            now_command = choice(list(commands.keys()))
            line = randint(0, len(self.game_start_matrix)) - 1

            if previous_command == now_command:
                repeat_command += 1
            else:
                repeat_command = 0
            if repeat_command == commands[now_command][1]:
                continue
            if previous_command != '' and commands[previous_command][0] * commands[now_command][0] == 1:
                continue

            if now_command.startswith("rotate"):
                eval(f"self.{now_command}()")
            elif now_command.startswith("shift_right"):
                eval(f"self.shift_right({line})")
            elif now_command.startswith("shift_down"):
                eval(f"self.shift_down({line})")

            mix -= 1

    def stop(self):
        self.RUN_GAME = False

    def is_win(self):
        start_and_left = self.np_matrix_start == self.np_matrix_left
        start_and_right = self.np_matrix_start == self.np_matrix_right
        return start_and_left.all() and start_and_right.all()

    def is_fail(self):
        if self.step < 1:
            if self.stars < 1:
                return True
            else:
                self.stars -= 1
                self.step = 10
        return False

    def is_running(self):
        return self.RUN_GAME

    def get_step(self):
        return self.step

    def get_stars(self):
        return self.stars

    def get_start_matrix(self):
        return self.game_start_matrix


if __name__ == '__main__':
    ...
