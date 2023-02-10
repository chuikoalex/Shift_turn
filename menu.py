import pygame
import pickle

import settings
import btn
import score


def save_game():
    """Функция сохранения достижений (не работает в DEMO)"""

    try:
        with open(f'save.save', 'wb') as file:
            pickle.dump(settings.score_player, file)
    except EOFError:
        return False
    return True


class Menu(pygame.sprite.Sprite):

    def __init__(self, group_sprites, game):
        super().__init__(group_sprites)
        self.game = game
        self.status_menu = 'full'
        self.image = pygame.Surface((settings.SIZE['WIN_WIDTH'], settings.SIZE['WIN_HEIGHT']))
        self.rect = self.image.get_rect()

        self.menu_buttons = pygame.sprite.Group()
        self.score_stars = pygame.sprite.Group()
        self.box_color = pygame.sprite.Group()

        self.btn_start = None
        self.btn_return = None

        self.setup_size = 3
        self.setup_color = 2
        self.setup_level = 1

        self.create_menu()
        self.update()

    def create_menu(self):
        """Функция построения меню."""

        self.image.fill(settings.bg_color)
        center_x, center_y = settings.SIZE['WIN_WIDTH'] // 2, settings.SIZE['WIN_HEIGHT'] // 2

        font = pygame.font.Font(settings.font_file, 90)

        # developer's name
        alex_box = pygame.Surface((150, 25)).convert_alpha()
        alex_box.fill(settings.bg_color)
        image_alex = pygame.image.load(f"img/@chuikoalex.png")
        alex_box.blit(image_alex, (0, 0))
        self.image.blit(alex_box, (settings.SIZE['WIN_WIDTH'] - 150, int(settings.SIZE['WIN_HEIGHT'] * 0.16)))
        # -----------------

        score.Score(self.score_stars, center_x, center_y - 180)

        btn.Button_menu(self.menu_buttons, "size3", center_x - 230 * 2, center_y - 75, "3 - 3", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "size5", center_x - 230, center_y - 75, "5 - 5", "btn_setup", active=False)
        btn.Button_menu(self.menu_buttons, "size7", center_x, center_y - 75, "7 - 7", "btn_setup", active=False)

        btn.Button_menu(self.menu_buttons, "color2", center_x - 230 * 2, center_y, "2..", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "color3", center_x - 230, center_y, "3...", "btn_setup")
        btn.Button_menu(self.menu_buttons, "color4", center_x, center_y, "4....", "btn_setup")

        btn.Button_menu(self.menu_buttons, "level1", center_x - 230 * 2, center_y + 75, ".-", "btn_setup", True)
        btn.Button_menu(self.menu_buttons, "level2", center_x - 230, center_y + 75, ".-..-", "btn_setup")
        btn.Button_menu(self.menu_buttons, "level3", center_x, center_y + 75, ".-..--..-", "btn_setup")

        self.btn_start = btn.Button_menu(self.menu_buttons, "start", center_x + 350, center_y + 75, "",
                                         "btn_run_game")
        self.btn_return = btn.Button_menu(self.menu_buttons, "return", center_x + 350, center_y + 150, "",
                                          "btn_return_game")

        setting_box = pygame.Surface((300, 140)).convert_alpha()
        image_shadow = pygame.image.load(f"img/{settings.skin}/setting_box.png")
        setting_box.blit(image_shadow, (0, 0))
        self.image.blit(setting_box, (center_x + 195, center_y - 110))

        shift_title = font.render("shift", True, settings.text_not_active_color)
        turn_title = font.render("turn", True, settings.text_not_active_color)
        self.image.blit(shift_title, (center_x - 460, center_y + 240))
        self.image.blit(turn_title, (center_x + 140, center_y + 240))

        btn.Box_color(self.box_color, center_x, center_y + 340, self.game.get_start_matrix())

        shadow = pygame.Surface((1, 10)).convert_alpha()
        image_shadow = pygame.image.load(f"img/{settings.skin}/shadow.png")
        shadow.blit(image_shadow, (0, 0))
        shadow = pygame.transform.scale(shadow, (settings.SIZE['WIN_WIDTH'], 10))
        self.image.blit(shadow, (0, settings.SIZE['WIN_HEIGHT'] - 10))

        self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.85)

    def update(self):
        if self.status_menu == "full":
            self.button_start_return_status()
            self.score_stars.draw(self.image)
            self.menu_buttons.update()
            self.menu_buttons.draw(self.image)
            self.box_color.draw(self.image)
            self.score_stars.update()

    def status(self):
        return self.status_menu

    def change_status(self):
        if self.status_menu == 'mini':
            self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.85)
            self.status_menu = 'full'
        elif self.status_menu == 'full':
            self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.20)
            self.status_menu = 'mini'

    def button_start_return_status(self):
        if self.game.is_running():
            self.btn_start.change_focus(True)
            self.btn_return.change_focus(True)
        else:
            self.btn_start.change_focus(False)
            self.btn_return.change_focus(False)

    def on_click(self, mouse_pos):
        """Функция обрабатывает нажатие мыши на объекты меню."""
        # Настроить нормальную работу кнопок, не должны кликаться во время игры...
        if mouse_pos[1] > settings.SIZE['WIN_HEIGHT'] * 0.85 and self.game.is_running():
            self.change_status()
            return
        for button_object in self.menu_buttons:
            button_object: btn.Button_menu
            return_code: str
            is_clicked, return_code = button_object.on_click((mouse_pos[0],
                                                              int(mouse_pos[1] + settings.SIZE['WIN_HEIGHT'] * 0.15)))
            if is_clicked:
                if return_code == 'start':
                    self.change_status()
                    self.game.run()
                    return
                elif return_code == 'return':
                    if self.game.is_running():
                        self.change_status()
                    return
                else:
                    for code in ["size", "color", "level"]:
                        if return_code.startswith(code):
                            self.game.stop()
                            for butt in self.menu_buttons:
                                butt: btn.Button_menu
                                if butt.get_return_code().startswith(code) and butt.get_focus():
                                    butt.change_focus()
                                    break
                            button_object.change_focus()
                            exec(f'self.setup_{code} = int(return_code[-1])')
                    if return_code.startswith("level"):
                        self.game.set_level(self.setup_level)
                    else:
                        self.game.set_attributes_matrix(self.setup_size, self.setup_color)
                break
        self.box_color.update(self.game.get_start_matrix())


if __name__ == '__main__':
    ...
