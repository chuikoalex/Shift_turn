import pygame
import pickle

import settings
import btn
import score


def save_game():
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

        self.setup_size = 3
        self.setup_color = 2
        self.setup_level = 1

        self.create()
        self.update()

    def create(self):
        self.image.fill(settings.bg_color)
        center_x, center_y = settings.SIZE['WIN_WIDTH'] // 2, settings.SIZE['WIN_HEIGHT'] // 2

        font = pygame.font.Font(settings.font_file, 90)

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

        btn.Button_menu(self.menu_buttons, "start", center_x + 350, center_y, "", "btn_run_game")
        btn.Button_menu(self.menu_buttons, "return", center_x + 350, center_y + 75, "", "btn_return_game")

        shift = font.render("shift", True, settings.text_not_active_color)
        turn = font.render("turn", True, settings.text_not_active_color)
        self.image.blit(shift, (center_x - 460, center_y + 240))
        self.image.blit(turn, (center_x + 140, center_y + 240))

        btn.Box_color(self.box_color, center_x, center_y + 340, self.game.get_start_matrix())

        shadow = pygame.Surface((1, 10)).convert_alpha()
        image_shadow = pygame.image.load(f"img/{settings.skin}/shadow.png")
        shadow.blit(image_shadow, (0, 0))
        shadow = pygame.transform.scale(shadow, (settings.SIZE['WIN_WIDTH'], 10))
        self.image.blit(shadow, (0, settings.SIZE['WIN_HEIGHT'] - 10))

        self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.85)

    def update(self):
        if self.status_menu == "full":
            self.menu_buttons.draw(self.image)
            # self.score_stars.update()  # - запускать только когда победил, для обновления счета
            self.score_stars.draw(self.image)
            self.box_color.draw(self.image)

    def status(self):
        return self.status_menu

    def change_status(self):
        if self.status_menu == 'mini':
            self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.85)
            self.status_menu = 'full'
        elif self.status_menu == 'full':
            self.rect.bottom = int(settings.SIZE['WIN_HEIGHT'] * 0.20)
            self.status_menu = 'mini'

    def on_click(self, mouse_pos):
        """Обрабатывает нажатие мыши на объекты меню"""
        for button_object in self.menu_buttons:
            button_object: btn.Button_menu
            return_code: str
            is_clicked, return_code = button_object.on_click((mouse_pos[0],
                                                              int(mouse_pos[1] + settings.SIZE['WIN_HEIGHT'] * 0.15)))
            if is_clicked:
                if return_code == 'start':
                    self.change_status()
                    ...  # изменить кнопки старта и возврата на активные
                    self.game.run()

                elif return_code == 'return':
                    self.change_status()
                else:
                    for code in ["size", "color", "level"]:
                        if return_code.startswith(code):
                            for butt in self.menu_buttons:
                                butt: btn.Button_menu
                                if butt.get_return_code().startswith(code) and butt.get_focus():
                                    butt.change_focus()
                                    break
                            button_object.change_focus()
                            exec(f'self.setup_{code} = int(return_code[-1])')
                    if not return_code.startswith("level"):
                        self.game.set_attributes_matrix(self.setup_size, self.setup_color)
                    else:
                        self.game.set_level(self.setup_level)
                    break

        self.menu_buttons.update()
        self.box_color.update(self.game.get_start_matrix())
        # self.setup_size, self.setup_color,self.setup_level


if __name__ == '__main__':
    ...
