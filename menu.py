import pygame

import settings
import btn


class Menu(pygame.sprite.Sprite):
    def __init__(self, group_sprites, game):
        super().__init__(group_sprites)
        self.status_menu = 'full'
        self.image = pygame.Surface((settings.WIN_WIDTH, settings.WIN_HEIGHT))
        self.rect = self.image.get_rect()

        self.menu_buttons = pygame.sprite.Group()

        self.create_menu()

    def create_menu(self):
        """Построение элементов в меню"""

        self.image.fill(settings.bg_color)
        center_x, center_y = settings.WIN_WIDTH // 2, settings.WIN_HEIGHT // 2

        font = pygame.font.Font("font/kenvector_future.ttf", 90)

        shift = font.render("shift", True, settings.text_not_active_color)
        turn = font.render("turn", True, settings.text_not_active_color)
        self.image.blit(shift, (center_x - 460, center_y + 250))
        self.image.blit(turn, (center_x + 140, center_y + 250))

        shadow = pygame.Surface((1, 10)).convert_alpha()
        image_shadow = pygame.image.load(f"img/{settings.skin}/shadow.png")
        shadow.blit(image_shadow, (0, 0))
        shadow = pygame.transform.scale(shadow, (settings.WIN_WIDTH, 10))
        self.image.blit(shadow, (0, settings.WIN_HEIGHT - 10))

        btn.Button_menu(self.menu_buttons, "size3", center_x - 230 * 2, center_y - 75, "3 - 3", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "size5", center_x - 230, center_y - 75, "5 - 5", "btn_setup", active=False)
        btn.Button_menu(self.menu_buttons, "size7", center_x, center_y - 75, "7 - 7", "btn_setup", active=False)

        btn.Button_menu(self.menu_buttons, "color2", center_x - 230 * 2, center_y, "2..", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "color3", center_x - 230, center_y, "3...", "btn_setup")
        btn.Button_menu(self.menu_buttons, "color4", center_x, center_y, "4....", "btn_setup")

        btn.Button_menu(self.menu_buttons, "level10", center_x - 230 * 2, center_y + 75, ".-", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "level20", center_x - 230, center_y + 75, ".-..-", "btn_setup")
        btn.Button_menu(self.menu_buttons, "level30", center_x, center_y + 75, ".-..--..-", "btn_setup")

        btn.Button_menu(self.menu_buttons, "start", center_x + 350, center_y, "", "btn_run_game")
        btn.Button_menu(self.menu_buttons, "return", center_x + 350, center_y + 75, "", "btn_return_game")

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

    def on_click(self, mouse_pos):
        """Обрабатывает нажатие мыши на объекты меню"""
        pass
