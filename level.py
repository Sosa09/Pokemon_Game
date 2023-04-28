import pygame
from settings import  *
from tile import Tile
from grass import Grass
from pokemons import *
from player import Player
from pokeball import Pokeball
from potion import Potion
class Level:

    def  __init__(self):
        #get display
        self.display_surface = pygame.display.get_surface()
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
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
                if col == '5':
                    Pokeball((x,y),[self.visible_sprites])
                if col == 'p':
                    Potion((x,y),[self.visible_sprites])
                if col == 'z':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                

class YsortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_heigth = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_heigth

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)