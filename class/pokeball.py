import pygame 

class Pokeball(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/pokeball.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = 'Pokeball'