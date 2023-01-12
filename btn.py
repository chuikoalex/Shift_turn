import pygame

import settings


class Button_menu(pygame.sprite.Sprite):
    image_btn = pygame.image.load(f"img/{settings.skin}/button_menu.png")

    def __init__(self, group_sprites, x, y, name, option, focus=False, active=True):
        super().__init__(group_sprites)
        self.x, self.y = x, y
        self.name = name
        self.option = option
        self.focus = focus
        self.active = active
        self.image = pygame.Surface((200, 45))
        self.image.blit(Button_menu.image_btn, (0, 0), settings.button_menu_position[option])
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        font = pygame.font.Font(settings.font_file, 30)
        text = font.render(name, True, (30, 167, 225))
        text_x = 100 - text.get_width() // 2
        text_y = 22 - text.get_height() // 2
        self.image.blit(text, (text_x, text_y))
        self.rect.center = x, y

    def on_click(self):
        status = None
        return status, self.name


class Button_game(pygame.sprite.Sprite):
    def __init__(self, group_sprites, name):
        super().__init__(group_sprites)
        self.name = name

    def on_click(self):
        status = None
        return status, self.name
