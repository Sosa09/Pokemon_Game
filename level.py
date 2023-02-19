import pygame
from settings import  *
from tile import Tile
from grass import Grass
from pokemon1 import Pokemon1
from pokemon2 import Pokemon2
from pokemon3 import Pokemon3
from pokemon4 import Pokemon4
from player import Player

class Level:

    def  __init__(self):
        #get display
        self.display_surface = pygame.display.get_surface()
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def run(self):
        #update
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()


    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'g':
                    Grass((x,y),[self.visible_sprites])
                if col == '1':
                    Pokemon1((x,y),[self.visible_sprites])
                if col == '2':
                    Pokemon2((x,y),[self.visible_sprites])
                if col == '3':
                    Pokemon3((x,y),[self.visible_sprites])
                if col == '4':
                    Pokemon4((x,y),[self.visible_sprites])
                if col == 'z':
                    self.player = Player((x,y),[self.visible_sprites])
                




