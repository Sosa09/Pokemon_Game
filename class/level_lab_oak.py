import pygame
from settings_lab_oak import  *
from tile import Tile
from pokemon import *
from player import Player
# from button import Button

class LevelLabOak:

    def  __init__(self):
        #get display from anywhere in our code!
        self.display_surface = pygame.display.get_surface()
        
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.pokemons = []
        

        self.create_map()

           

    def run(self):
        #update
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == '1':
                    self.pokemons.append(Pokemon1((x,y),[self.visible_sprites]))
                if col == '2':
                    self.pokemons.append(Pokemon2((x,y),[self.visible_sprites]))
                if col == '3':
                    self.pokemons.append(Pokemon3((x,y),[self.visible_sprites]))
                if col == 'z':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self, player):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
           
                