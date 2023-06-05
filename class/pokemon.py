import pygame

class Pokemon1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('Images/Pokemons/bulbasaur0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Bulbasaur"


class Pokemon2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('Images/Pokemons/charizard.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "charizard"

class Pokemon3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('Images/3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "poesje"

class Pokemon4(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('Images/4.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "ratje"
        
        
