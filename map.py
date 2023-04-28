import pygame, sys
from settings import *
from level import Level
import time

class Game:

    def __init__(self):

        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('POKEMON SYNTRA')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            color = (61,145,64)
            self.screen.fill(color)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            # counter = 0
            # while counter != 5:
            #     battle = pygame.Surface((200,400))
            #     self.screen.blit(battle,(600,360))
            #     pygame.display.update()
            #     self.clock.tick(FPS)
            #     time.sleep(1)
            #     counter +=1
            # pygame.display.update()
            # self.clock.tick(FPS)




if __name__=='__main__':
    game = Game()
    game.run()