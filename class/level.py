# created and managed by Tanguy, modified by Soufiane
import pygame, json, copy
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
        self.pokemons = []
        self.items = []
        self.list_pokemons = []
        self.pokemon_choice = []
        self._load_pokemons()
        self.create_map()
        # going to add a button to pause the game (added by Joris)  
        self.create_button()
     
    #declare a list variable to store the pokemons
    def _load_pokemons(self):
        

        index = 0
        #extract all pokemons from the json database and loop into pokemon table and initialize a pokemon instance to store all pokemon into list_pokemons
        with open('Database/pokemons_db.json', 'r') as file:
            json_data = json.load(file)

            for pokemon in json_data["pokemons"]:
                try:
                    
                    iPokemon = Pokemon(pokemon["name"],pokemon["type"],pokemon["hp"],pokemon["at"],pokemon["df"],pokemon["spa"],pokemon["spdef"],pokemon["spd"],pokemon["img"])
                    self.list_pokemons.append(iPokemon)
                    if index < 3:
                        poke_choice = Pokemon(pokemon["name"],pokemon["type"],pokemon["hp"],pokemon["at"],pokemon["df"],pokemon["spa"],pokemon["spdef"],pokemon["spd"],pokemon["img"])
                        self.pokemon_choice.append(poke_choice)
                    index = index + 1
                except Exception as e:
                    print(e)
    

    def run(self):
        #update
        self.visible_sprites.custom_draw(self.player, self.pokemons)
        self.visible_sprites.update()
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                elif col == 'g':
                    Grass((x,y),[self.visible_sprites])
                elif col == '1':
                    p  = self.list_pokemons[0]
                    p.set_position((x,y))
                    p.set_groups([self.visible_sprites])
                    self.pokemons.append(p)
                elif col == '2':
                    p  = self.list_pokemons[1]
                    p.set_groups([self.visible_sprites])
                    p.set_position((x,y))
                    
                    self.pokemons.append(p)
                elif col == '3':
                    p  = self.list_pokemons[2]
                    p.set_groups([self.visible_sprites])
                    p.set_position((x,y))
                    
                    self.pokemons.append(p) 
                elif col == '4':
                    p  = self.list_pokemons[3]
                    p.set_position((x,y))
                    p.set_groups([self.visible_sprites])
                    self.pokemons.append(p)
                elif col == '5':
                    p  = self.list_pokemons[4]
                    p.set_position((x,y))
                    p.set_groups([self.visible_sprites])
                    self.pokemons.append(p)
                elif col == 'b':

                    self.items.append(Pokeball((x,y),[self.visible_sprites]))
                elif col == 'p':
                   
                   self.items.append(Potion((x,y),[self.visible_sprites]))
                elif col == 'z':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                    self.player.pokemons.append(self.pokemon_choice[0])
                    
    def create_button(self):
        font = pygame.font.SysFont(None, 30)
        text_color = (255, 255, 255)
        button_color = (50, 50, 50)
        hover_color = (100, 100, 100)
        new_Button = Button(100, 100, 200, 50, "Pause", font, text_color, button_color, hover_color)
        new_Button.draw(self.display_surface)            
                
class YsortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_heigth = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player, pokemons):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_heigth
        for pokemon in pokemons:
            offset_pos = pokemon.rect.topleft - self.offset
            self.display_surface.blit(pokemon.image,offset_pos)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)