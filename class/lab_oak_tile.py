import pygame
from lab_oak_settings import *

class LabOakTile(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('images/boom.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (20,20))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0) # changed for collision
        