"""Программа shift-turn"""
import pygame

import settings
from menu import Menu
from board import Board
from game import Game

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shift_turn')
    size = settings.WIN_WIDTH, settings.WIN_HEIGHT
    window = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    menu_sprites = pygame.sprite.Group()
    menu = Menu(menu_sprites)

    game = Game()

    board = Board(window)

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
                elif event.key == pygame.K_UP and event.mod == pygame.KMOD_LCTRL:
                    pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass

        menu_sprites.draw(window)
        pygame.display.flip()
        clock.tick(settings.FPS)
    pygame.quit()
