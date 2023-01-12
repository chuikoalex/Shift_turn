import pygame

import settings
import btn


class Menu(pygame.sprite.Sprite):
    def __init__(self, group_sprites):
        super().__init__(group_sprites)
        self.status_menu = 'full'
        self.size = settings.WIN_WIDTH, settings.WIN_HEIGHT
        self.image = pygame.Surface((settings.WIN_WIDTH, settings.WIN_HEIGHT))
        self.rect = self.image.get_rect()


        self.menu_buttons = pygame.sprite.Group()

        self.create_menu()

    def create_menu(self):
        """Построение элементов в меню"""
        self.image.fill('grey')
        btn.Button_menu(self.menu_buttons, 200, 300, "3 - 3", "btn_focus_off", )
        self.rect.bottom = int(settings.WIN_HEIGHT * 0.85)

        self.menu_buttons.draw(self.image)

    def draw(self):
        if self.status_menu == "full":
            self.menu_buttons.draw(self.image)

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
