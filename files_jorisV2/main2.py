import pygame
import sys
from settings import Settings
from menuscreen import MenuScreen

class RunGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.get_screen_width(), self.settings.get_screen_height()))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.current_screen = MenuScreen()

    def run(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.current_screen.handle_events(event)

    def update(self):
        self.current_screen.update()

    def draw(self):
        self.current_screen.draw(self.screen)
        pygame.display.flip()

game = RunGame()
game.run()
