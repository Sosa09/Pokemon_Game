# Created and managed by Soufaine
import pygame
from settings import *
class Trainer(pygame.sprite.Sprite):
    def __init__(self, groups,name = "", age = 0):
        super().__init__(groups)
        self.pygame = pygame
        self.name = name
        self.age = age
        self.pokemons = [] #determined by the pokemon choice and the catches GOTTA CATCH M ALL

    def greet(self):
        pass
    def __str__(self):
        #trainer's info
        pass