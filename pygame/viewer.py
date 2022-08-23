import pygame


class Viewer:
    def __init__(self, update_func, display_size):
        self.running = False
        self.update_func = update_func
        self.display = pygame.display.set_mode(display_size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            update_func = self.update_func()
            surface = pygame.surfarray.make_surface(update_func)
            self.display.blit(pygame.transform.scale(surface, self.display.get_rect().size), (0, 0))

            pygame.display.update()

        pygame.quit()
