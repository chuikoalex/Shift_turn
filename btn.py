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

    def get_focus(self):
        return self.focus

    def on_click(self, pos):
        if self.active:
            click = self.rect.collidepoint(pos)
            return click, self.return_code
        return False, ''


class Button_game(pygame.sprite.Sprite):
    def __init__(self, group_sprites, name):
        super().__init__(group_sprites)
        self.name = name

    def on_click(self):
        status = None
        return status, self.name
