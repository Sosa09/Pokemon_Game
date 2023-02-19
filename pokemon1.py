import pygame

class Pokemon1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)