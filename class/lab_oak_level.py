import pygame
from lab_oak_settings import  *
from lab_oak_tile import LabOakTile
from lab_oak_tile_exit import LabOakTileExit
from lab_oak_prof_oak import *
from lab_oak_pokemon import *
from player import Player
# from button import Button

class LevelLabOak:

    def  __init__(self):
        #get display from anywhere in our code!
        self.display_surface = pygame.display.get_surface()
        
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.pokemons = []
        self.exit = []
        self.create_map()

           

    def run(self):
        for sprite in self.visible_sprites:
            if isinstance(sprite, LabOakTile):
                continue  # Skip drawing LabOakTile objects (had error bc lab_oak_tile had no more image)
            if isinstance(sprite, LabOakTileExit):
                continue  # Skip drawing LabOakTile objects (had error bc lab_oak_tile had no more image)
            if hasattr(sprite, 'image'):  # Check if the sprite has an image attribute
                self.display_surface.blit(sprite.image, sprite.rect)  # Draw the sprite's image
        
        self.visible_sprites.update()


    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    LabOakTile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'd':
                    self.exit.append(LabOakTileExit((x,y),[self.visible_sprites,self.obstacle_sprites]))
                if col == 'o':
                    ProfessorOak((x,y), [self.visible_sprites, self.obstacle_sprites])
                if col == '1':
                    self.pokemons.append(Pokemon((x,y),[self.visible_sprites], "Bulbasaur", "Images/Pokemons/bulbasaur0.png"))
                if col == '2':
                    self.pokemons.append(Pokemon((x,y),[self.visible_sprites], "Charmander", "Images/Pokemons/charmander.png"))
                if col == '3':
                    self.pokemons.append(Pokemon((x,y),[self.visible_sprites], "Squirtle", "Images/Pokemons/squirtle.png"))
                if col == 'z':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
    

           
                