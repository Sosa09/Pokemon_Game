import pygame, sys
from settings import  *
from player import Player

class Game:

    def __init__(self):

        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('POKEMON SYNTRA')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # Load the background image
            background_image = pygame.image.load("images\oak.jpg")

            # Resize the background image to fit the display window
            background_image = pygame.transform.scale(background_image, (1000, 600))

            # Blit the background image onto the screen
            self.screen.blit(background_image, (0, 0))  
            pygame.display.update()
            self.clock.tick(FPS)

if __name__=='__main__':
    game = Game()
    game.run()