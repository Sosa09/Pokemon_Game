# Created and managed by Soufiane
import pygame

class Pokemon(pygame.sprite.Sprite):

    def __init__(self, pos, groups, name, path):
        super().__init__(groups)
        self.name = name
        self.path = path
        self.pos = pos
        self._load_image()
        
    def _load_image(self):
        self.image = pygame.image.load(f'{self.path}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft = self.pos)
        
