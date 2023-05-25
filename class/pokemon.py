import pygame

class Pokemon1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/Pokemons/bullbizar.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Bullbizar"


class Pokemon2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/Pokemons/charizard.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "charizard"

class Pokemon3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Pokemon4(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/4.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        
