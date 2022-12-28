import pygame

import settings


class Menu(pygame.sprite.Sprite):
    def __init__(self, group_sprites):
        super().__init__(group_sprites)
        self.status_menu = 'full'
        self.size = settings.WIN_WIDTH, settings.WIN_HEIGHT
        self.image = pygame.Surface((settings.WIN_WIDTH, settings.WIN_HEIGHT))
        self.image.fill('grey')
        self.rect = self.image.get_rect()
        self.rect.bottom = int(settings.WIN_HEIGHT * 0.85)

    def create_menu(self):
        """Построение элементов в меню"""
        pass

    def status(self):
        return self.status_menu

    def change_status(self):
        if self.status_menu == 'mini':
            self.rect.bottom = int(settings.WIN_HEIGHT * 0.85)
            self.status_menu = 'full'
        elif self.status_menu == 'full':
            self.rect.bottom = int(settings.WIN_HEIGHT * 0.15)
            self.status_menu = 'mini'

    def on_click(self):
        """Обрабатывает нажатие мыши на объекты меню"""
        pass

    def get_click(self, mouse_pos):
        """Возвращает код нажатого (динамического) объекта"""
        pass
