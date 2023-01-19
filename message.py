import pygame

import settings


class Message(pygame.sprite.Sprite):
    image_no = pygame.image.load(f"img/{settings.skin}/no.png")
    image_yes = pygame.image.load(f"img/{settings.skin}/yes.png")

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        self.font = pygame.font.Font(settings.font_file, 60)

    def show_message(self, text, window, yes=False, no=False):
        text = self.font.render(text, True, settings.text_not_active_color)

        self.image = pygame.Surface((text.get_width() + 280, 80))
        self.rect = self.image.get_rect()

        self.image.fill('white')
        self.image.blit(text, (0, 5))
        self.image.blit(Message.image_yes, (text.get_width() + 50, 15))
        self.image.blit(Message.image_no, (text.get_width() + 180, 15))

        self.rect.bottom = settings.SIZE['WIN_HEIGHT']

        window.blit(self.image, (settings.SIZE['WIN_WIDTH'] // 2 - self.image.get_width() // 2,
                                 settings.SIZE['WIN_HEIGHT'] - 100))
        pygame.display.update((0, settings.SIZE['WIN_HEIGHT'] - 100,
                               settings.SIZE['WIN_WIDTH'], settings.SIZE['WIN_HEIGHT']))

        yes_pos_x = settings.SIZE['WIN_WIDTH'] // 2 + self.image.get_width() // 2 - 180
        no_pos_x = settings.SIZE['WIN_WIDTH'] // 2 + self.image.get_width() // 2 - 50
        yes_no_pos_y = self.rect.bottom

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if yes:
                            if (yes_pos_x - 50) < event.pos[0] < (yes_pos_x + 50):
                                if (yes_no_pos_y - 90) < event.pos[1] < (yes_no_pos_y - 30):
                                    return True
                        if no:
                            if (no_pos_x - 50) < event.pos[0] < (no_pos_x + 50):
                                if (yes_no_pos_y - 90) < event.pos[1] < (yes_no_pos_y - 30):
                                    return False
