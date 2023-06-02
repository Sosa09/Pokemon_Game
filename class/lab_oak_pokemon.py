import pygame

class Pokemon1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('Images/Pokemons/bulbasaur0.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Bullbizar"


class Pokemon2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('Images/Pokemons/charizard.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Charizard"

class Pokemon3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('Images/3.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Ivysaur"

        
        
