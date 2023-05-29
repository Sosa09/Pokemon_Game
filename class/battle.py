#created, maintained by Soufiane
import pygame
from settings import *

# define your class
class Battle():
    
    # initializes a new instance of Battle class
    def __init__(self):
        pass
    #Define Battle function
    def _start_battle(self, obj):
        # Starts the battle loop using pygame
        # Set the game loop state
        battleState = True
        # Add an excepetion to catch errors and avoid the game to crashe
        try:
            # begin the game loop
            while(battleState): 
                # Loop trugh the built in event.get function of the pygame library
                # chceck if the game is quitting then exit
                # if esc is pressed end the battle
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        battleState = False
                    if event.key == pygame.K_ESCAPE:
                        #remove element after it has collided
                        obj.groups.remove(obj.collidedItem)
                        obj.level.pokemons.remove(obj.collidedItem)
                        # Update groups
                        obj.collidedItem.image = pygame.Surface((0,0))
                        obj.groups.update()
                        battleState = False
                        obj.run()
                # Create a font object
                font = pygame.font.SysFont("Arial", 30)
                
                # Render the text
                text_surface = font.render(f"Battle Begins!\nTrainer: Ash VS {obj.collidedItem.name}\nclick on the screen to go back", True, (0, 0, 0))                # Position the text
                text_rect = text_surface.get_rect()
                text_rect.center = (400, 300)
                # Fill the background in white
                obj.screen.fill("white")
                # draw it on the screen
                obj.screen.blit(text_surface, text_rect)
           
                #update the display
                pygame.display.update()              
        except Exception as e:
            print(e)
    