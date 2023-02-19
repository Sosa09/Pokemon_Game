import pygame

class Pokemon3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)