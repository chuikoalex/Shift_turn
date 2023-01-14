import pygame

import settings


class Button_menu(pygame.sprite.Sprite):
    image_btn = pygame.image.load(f"img/{settings.skin}/button_menu.png")

    def __init__(self, group_sprites, return_code, position_x, position_y, text, option, focus=False, active=True):
        super().__init__(group_sprites)
        self.return_code = return_code
        self.x, self.y = position_x, position_y
        self.text = text
        self.option = option
        self.focus = focus
        self.active = active
        if self.active:
            self.font_color = settings.text_active_color
        else:
            self.font_color = settings.text_not_active_color

        self.update()

    def update(self):
        self.image = pygame.Surface((200, 45)).convert_alpha()
        self.rect = self.image.get_rect()

        self.image.fill(settings.bg_color)
        self.image.blit(Button_menu.image_btn, (0, 0), settings.button_menu_position[self.option][self.focus])

        font = pygame.font.Font(settings.font_file, settings.font_size)
        text = font.render(self.text, True, self.font_color)
        self.image.blit(text, (100 - text.get_width() // 2, 22 - text.get_height() // 2))

        self.rect.center = self.x, self.y

    def change_focus(self):
        self.focus = False if self.focus else True

    def get_return_code(self):
        return self.return_code

    def get_option(self):
        return self.option

    def get_focus(self):
        return self.focus

    def get_active(self):
        return self.active

    def on_click(self, pos):
        if self.active:
            click = self.rect.collidepoint(pos)
            return click, self.return_code
        return False, ''


class Box_color(pygame.sprite.Sprite):
    image_box_color = {0: pygame.image.load(f"img/{settings.skin}/{settings.box_image['grey']}"),
                       1: pygame.image.load(f"img/{settings.skin}/{settings.box_image['blue']}"),
                       2: pygame.image.load(f"img/{settings.skin}/{settings.box_image['green']}"),
                       3: pygame.image.load(f"img/{settings.skin}/{settings.box_image['red']}"),
                       4: pygame.image.load(f"img/{settings.skin}/{settings.box_image['yellow']}"),
                       }

    def __init__(self, group_sprites, position_x, position_y, matrix):
        super().__init__(group_sprites)
        self.x, self.y = position_x, position_y

        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        self.update(matrix)

    def update(self, matrix):
        height = Box_color.image_box_color[0].get_height()
        size = len(matrix) * height
        self.image = pygame.Surface((size, size)).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill(settings.bg_color)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                img = Box_color.image_box_color[matrix[row][col]]
                self.image.blit(img, (0 + col * height, 0 + row * height))

        self.rect.center = self.x, self.y - size // 2


class Button_game(pygame.sprite.Sprite):
    def __init__(self, group_sprites, name):
        super().__init__(group_sprites)
        self.name = name

    def on_click(self):
        status = None
        return status, self.name
