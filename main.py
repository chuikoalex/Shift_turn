"""Программа shift-turn"""
import pygame

import settings
from menu import Menu
from board import Board
from game import Game


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shift_turn')
    pygame.display.set_icon(pygame.image.load('shift-turn.png'))
    size = settings.SIZE['WIN_WIDTH'], settings.SIZE['WIN_HEIGHT']
    window = pygame.display.set_mode(size)

    game = Game()

    menu_sprites = pygame.sprite.Group()
    menu = Menu(menu_sprites, game)

    board_sprites = pygame.sprite.Group()
    board = Board(board_sprites, game)

    clock = pygame.time.Clock()
    RUNNING = True
    while RUNNING:
        window.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu.change_status()
                if event.key == pygame.K_ESCAPE:
                    if menu.status() == 'mini':
                        menu.change_status()
                    else:
                        RUNNING = False
                        continue
                elif event.key == pygame.K_UP and event.mod == pygame.KMOD_LCTRL:
                    pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu.status() == 'full':
                    menu.on_click(event.pos)
                else:
                    board.on_click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                ...
            if event.type == pygame.MOUSEMOTION:
                ...
        board_sprites.update()
        board_sprites.draw(window)
        menu_sprites.update()
        menu_sprites.draw(window)

        pygame.display.flip()
        clock.tick(settings.FPS)
    pygame.quit()
