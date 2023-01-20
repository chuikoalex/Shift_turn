"""Программа shift-turn"""
import pygame

import settings
from menu import Menu
from board import Board
from game import Game
from message import Message


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
    board = Board(board_sprites, window, game)

    message = Message()

    VICTORY = None

    clock = pygame.time.Clock()
    RUNNING = True
    while RUNNING:
        window.fill('white')
        if VICTORY == 'win':
            message.show_message("YOU WIN!!!", window, True)
            VICTORY = None
        elif VICTORY == 'fail':
            message.show_message("FAIL...", window, True)
            VICTORY = None
        elif VICTORY == 'pause':
            VICTORY = None
            menu.change_status()
        if not game.is_running() and menu.status() == "mini":
            menu.change_status()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.is_running():
                    menu.change_status()
                if event.key == pygame.K_ESCAPE:
                    if menu.status() == 'mini':
                        menu.change_status()
                    else:
                        if message.show_message('QUIT?', window, True, True):
                            RUNNING = False
                            continue

            if event.type == pygame.KEYUP:
                ...
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu.status() == 'full':
                    menu.on_click(event.pos)
                else:
                    VICTORY = board.on_click(event.pos)
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
