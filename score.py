import pygame

import settings


class Score(pygame.sprite.Sprite):
    image_stars = pygame.image.load(f"img/{settings.skin}/stars.png")

    def __init__(self, group_sprites, position_x, position_y):
        super().__init__(group_sprites)
        self.x, self.y = position_x, position_y
        self.font = pygame.font.Font(settings.font_file, 64)

        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        score_gold = self.font.render(f' {settings.score_player["gold"]} ', True, settings.text_not_active_color)
        score_green = self.font.render(f' {settings.score_player["green"]} ', True, settings.text_not_active_color)
        score_blue = self.font.render(f' {settings.score_player["blue"]}', True, settings.text_not_active_color)
        score_width = score_gold.get_width() + score_green.get_width() + score_blue.get_width()
        self.image = pygame.Surface((210 + score_width, 64)).convert_alpha()
        self.rect = self.image.get_rect()

        self.image.fill(settings.bg_color)

        self.image.blit(Score.image_stars, (0, 0),
                        settings.stars["gold"])
        self.image.blit(score_gold, (70, 0))

        self.image.blit(Score.image_stars, (70 + score_gold.get_width(), 0),
                        settings.stars["green"])
        self.image.blit(score_green, (140 + score_gold.get_width(), 0))

        self.image.blit(Score.image_stars, (140 + score_gold.get_width() + score_green.get_width(), 0),
                        settings.stars["blue"])
        self.image.blit(score_blue, (210 + score_gold.get_width() + score_green.get_width(), 0))

        self.rect.center = self.x, self.y
