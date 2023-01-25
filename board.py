import pygame

import settings
import score
import tiles
import btn
from message import Message


class Board(pygame.sprite.Sprite):

    def __init__(self, group_sprites, window, game):
        super().__init__(group_sprites)
        self.window = window
        self.game = game
        self.message_board = Message()
        self.image = pygame.Surface((settings.SIZE['WIN_WIDTH'], settings.SIZE['WIN_HEIGHT']))
        self.center_x, self.center_y = settings.SIZE['WIN_WIDTH'] // 2, settings.SIZE['WIN_HEIGHT'] // 2
        self.rect = self.image.get_rect()

        self.score_step = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.buttons_board = pygame.sprite.Group()

        self.create()

    def create(self):
        self.image.fill('white')
        score.Step(self.score_step, self.center_x, self.center_y)
        tiles.Tiles_left(self.tiles, self.center_x - 300, self.center_y, self.game)
        tiles.Tiles_right(self.tiles, self.center_x + 300, self.center_y, self.game)
        self.update()

    def update(self):
        self.score_step.update(self.game.get_step(), self.game.get_stars())
        self.score_step.draw(self.image)

        self.tiles.update()
        self.tiles.draw(self.image)

        self.buttons_board.update()
        self.buttons_board.draw(self.image)

        self.draw_buttons()

    def draw_buttons(self):
        btn.Button_board(self.buttons_board, self.center_x - 364, self.center_y - 128, "rotate_right")
        btn.Button_board(self.buttons_board, self.center_x + 236, self.center_y - 128, "rotate_right", True)

        btn.Button_board(self.buttons_board, self.center_x - 236, self.center_y - 128, "shift_right_long")
        btn.Button_board(self.buttons_board, self.center_x + 364, self.center_y - 128, "shift_right_long", True)

        btn.Button_board(self.buttons_board, self.center_x - 172, self.center_y - 64,
                         "shift_right_short", False, 0)
        btn.Button_board(self.buttons_board, self.center_x + 428, self.center_y - 64,
                         "shift_right_short", True, 0)
        btn.Button_board(self.buttons_board, self.center_x - 172, self.center_y,
                         "shift_right_short", False, 1)
        btn.Button_board(self.buttons_board, self.center_x + 428, self.center_y,
                         "shift_right_short", True, 1)
        btn.Button_board(self.buttons_board, self.center_x - 172, self.center_y + 64,
                         "shift_right_short", False, 2)
        btn.Button_board(self.buttons_board, self.center_x + 428, self.center_y + 64,
                         "shift_right_short", True, 2)

        btn.Button_board(self.buttons_board, self.center_x - 236, self.center_y + 128,
                         "shift_down_short", False, 2)
        btn.Button_board(self.buttons_board, self.center_x + 364, self.center_y + 128,
                         "shift_down_short", True, 2)
        btn.Button_board(self.buttons_board, self.center_x - 300, self.center_y + 128,
                         "shift_down_short", False, 1)
        btn.Button_board(self.buttons_board, self.center_x + 300, self.center_y + 128,
                         "shift_down_short", True, 1)
        btn.Button_board(self.buttons_board, self.center_x - 364, self.center_y + 128,
                         "shift_down_short", False, 0)
        btn.Button_board(self.buttons_board, self.center_x + 236, self.center_y + 128,
                         "shift_down_short", True, 0)

        btn.Button_board(self.buttons_board, self.center_x - 428, self.center_y + 64, "shift_down_long")
        btn.Button_board(self.buttons_board, self.center_x + 172, self.center_y + 64, "shift_down_long", True)

        btn.Button_board(self.buttons_board, self.center_x - 428, self.center_y - 64, "rotate_down")
        btn.Button_board(self.buttons_board, self.center_x + 172, self.center_y - 64, "rotate_down", True)

    def on_click(self, mouse_pos):
        """Обрабатывает нажатие мыши на объекты меню"""
        if mouse_pos[1] < settings.SIZE['WIN_HEIGHT'] * 0.19:
            return 'pause'
        if self.game.is_running():
            for button_object in self.buttons_board:
                button_object: btn.Button_board
                return_code: str
                is_clicked, return_code, line = button_object.on_click(mouse_pos)
                if is_clicked:
                    result = self.game.signal_from_board(return_code, line)
                    return result
        return None


if __name__ == '__main__':
    ...
