from start import start
from pokemon import pokemon
from map import map
from trainer import trainer
import pygame, battle

s = start()

pokemons = list()
pokemons.append(s.load_pokemons())

selected_pokemon = list()
selected_pokemon.append(s.select_pokemon())

tra = trainer("Soufiane", selected_pokemon, 5)

print(tra.greet())

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# #define trainer x, y (load image of trainer later) start position
# trainer_x = 50
# trainer_y = 50

# #set running game to true until quiting the game
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
# pygame.quit()