import pygame

import settings


class Tiles:
    image_tiles = {0: pygame.image.load(f"img/{settings.skin}/{settings.tile_image['grey']}"),
                   1: pygame.image.load(f"img/{settings.skin}/{settings.tile_image['blue']}"),
                   2: pygame.image.load(f"img/{settings.skin}/{settings.tile_image['green']}"),
                   3: pygame.image.load(f"img/{settings.skin}/{settings.tile_image['red']}"),
                   4: pygame.image.load(f"img/{settings.skin}/{settings.tile_image['yellow']}"),
                   }


class Tiles_left(pygame.sprite.Sprite, Tiles):
    def __init__(self, group_sprites, position_x, position_y, game):
        super().__init__(group_sprites)
        self.x, self.y = position_x, position_y
        self.game = game

        self.image = pygame.Surface((1, 1))
        self.update()

    def update(self):
        matrix_left = self.game.get_matrix_left()
        self.image = pygame.Surface((64 * len(matrix_left), 64 * len(matrix_left))).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill('white')
        for row in range(len(matrix_left)):
            for col in range(len(matrix_left[row])):
                img = Tiles.image_tiles[matrix_left[row][col]]
                self.image.blit(img, (0 + col * 64, 0 + row * 64))
        self.rect.center = self.x, self.y


class Tiles_right(pygame.sprite.Sprite, Tiles):
    def __init__(self, group_sprites, position_x, position_y, game):
        super().__init__(group_sprites)
        self.x, self.y = position_x, position_y
        self.game = game

        self.image = pygame.Surface((1, 1))
        self.update()

    def update(self):
        matrix_right = self.game.get_matrix_right()
        self.image = pygame.Surface((64 * len(matrix_right), 64 * len(matrix_right))).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill('white')
        for row in range(len(matrix_right)):
            for col in range(len(matrix_right[row])):
                img = Tiles.image_tiles[matrix_right[row][col]]
                self.image.blit(img, (0 + col * 64, 0 + row * 64))
        self.rect.center = self.x, self.y
