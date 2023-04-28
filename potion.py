import pygame

class Potion(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/potion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)