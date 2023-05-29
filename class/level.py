# created and managed by Tanguy
import pygame
from settings import  *
from tile import Tile
from grass import Grass
from pokemon import *
from player import Player
from pokeball import Pokeball
from potion import Potion
from button import Button


class Level:

    def  __init__(self):
        #get display
        self.display_surface = pygame.display.get_surface()
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.pokebag = []
        self.create_map()
        # going to add a button to pause the game (added by Joris)  
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.hover_color = (100, 100, 100)
        self.create_button()
        
       

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
                    self.pokebag.append(Pokemon1((x,y),[self.visible_sprites]))
                if col == '2':
                    self.pokebag.append(Pokemon2((x,y),[self.visible_sprites]))
                if col == '3':
                    self.pokebag.append(Pokemon3((x,y),[self.visible_sprites]))
                if col == '4':
                    self.pokebag.append(Pokemon4((x,y),[self.visible_sprites]))
                if col == '5':
                    self.pokebag.append(Pokeball((x,y),[self.visible_sprites]))
                if col == 'p':
                    self.pokebag.append(Potion((x,y),[self.visible_sprites]))
                if col == 'z':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                if col == 'y':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
    
    def create_button(self):
        new_Button = Button(100, 100, 200, 50, "Pause", self.font, self.text_color, self.button_color, self.hover_color)
        new_Button.draw(self.display_surface)            
                

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