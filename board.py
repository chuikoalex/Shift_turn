import pygame
import numpy

import settings
import btn


class Board(pygame.sprite.Sprite):

    def __init__(self, group_sprites, game):
        super().__init__(group_sprites)
        self.game = game
        self.image = pygame.Surface((settings.SIZE['WIN_WIDTH'], settings.SIZE['WIN_HEIGHT']))
        self.rect = self.image.get_rect()
        self.image.fill('white')

    def update(self):
        self.draw_box_stars()
        self.draw_tiles()
        self.draw_buttons()

    def draw_box_stars(self):
        """Отрисовка центрального блока со звездочками и количеством ходов"""
        pass

    def draw_tiles(self):
        """Отрисовка левого и правого(обратного) набора тайлов"""
        pass

    def draw_buttons(self):
        """Отрисовка кнопок вокруг тайлов"""
        pass

    def on_click(self, pos):
        """Обрабатывает нажатие мыши на объекты меню"""
        if self.game.get_status():
            print("board_click")


if __name__ == '__main__':
    ...
