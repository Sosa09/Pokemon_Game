import pygame
from lab_oak_settings import *

class LabOakTile(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.rect = pygame.Rect(pos, (TILESIZE, TILESIZE))
        self.hitbox = self.rect.inflate(0, 0)  # changed for collision

    def update(self):
        pass  # You can add any additional logic or updates here
        