"""
Настройки программы по умолчанию
"""
WIN_WIDTH = 1280
WIN_HEIGHT = 720
FPS = 60


# img/папка с изображениями
skin = "skin_rock"
# цвет фона
bg_color = (238, 238, 238)

# настройки шрифта
font_file = "font/kenvector_future.ttf"
font_size = 24
text_active_color = (30, 167, 225)
text_not_active_color = (159, 159, 159)

# изображения центрального бокса с ходами и звездами
box_stars_image = {0: "box_stars_0.png",
                   1: "box_stars_1.png",
                   2: "box_stars_2.png",
                   3: "box_stars_3.png"}

# изображения тайлов
tile_image = {"blue": "tile_blue_64.png",
              "green": "tile_green_64.png",
              "red": "tile_red_64.png",
              "yellow": "tile_yellow_64.png",
              "grey": "tile_grey_64.png"
              }

# изображение кнопок меню и их позиционирование
button_menu_image = "button_menu.png"
button_menu_position = {"btn_setup": [(0, 0, 200, 45), (200, 0, 200, 45)],
                        "btn_run_game": [(0, 45, 200, 45), (200, 45, 200, 45)],
                        "btn_return_game": [(0, 90, 200, 45), (200, 90, 200, 45)]
                        }
