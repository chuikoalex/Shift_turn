import pygame
import numpy

import settings


class Board:
    def __init__(self, window):
        pass

    def create_tables(self, size):
        """Создание таблиц хранящих в себе расположение тайлов"""
        pass

    def modification_tables(self, code):
        """Изменение таблиц в соответствии с полученным кодом
        коды:
        """
        pass

    def draw_box_stars(self):
        """Отрисовка центрального блока со звездочками и количеством ходов"""
        pass

    def draw_tiles(self):
        """Отрисовка левого и правого(обратного) набора тайлов"""
        pass

    def draw_buttons(self):
        """Отрисовка кнопок вокруг тайлов"""
        pass

    def draw_board(self):
        """Отрисовка всего игрового поля"""
        pass

    def on_click(self):
        """Обрабатывает нажатие мыши на объекты меню"""
        pass

    def get_click(self, mouse_pos):
        """Возвращает код нажатого (динамического) объекта"""
        pass
