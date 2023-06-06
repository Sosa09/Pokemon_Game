import pygame
import json

class Pokemon(pygame.sprite.Sprite):

    def __init__(self, pos, groups, name, path):
        super().__init__(groups)
        self.name = name
        self.path = path
        self.pos = pos
        self._load_image()

        
    def _load_image(self):
        self.image = pygame.image.load(f'{self.path}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (41, 42))
        self.rect = self.image.get_rect(topleft = self.pos)
        return self.image


    def update(self):
        # Update the Pokémon state, position, etc.
        pass

        






























class Pokemon1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('Images/Pokemons/bulbasaur0.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Bulbasaur"


class Pokemon2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('Images/Pokemons/charmander.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Charmander"


class Pokemon3(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        test = pygame.image.load('images\Pokemons\squirtle.png').convert_alpha()
        self.image =  pygame.transform.scale(test, (41,42))
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "Squirtle"

        
        
