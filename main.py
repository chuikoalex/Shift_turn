import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('shift_turn')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    fps = 60
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('event key_down space')
                elif event.key == pygame.K_UP and event.mod == pygame.KMOD_LCTRL:
                    pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f'event mouse_down {event.button}')
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEMOTION:
                print(f'event mouse_move {event.pos}')

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
