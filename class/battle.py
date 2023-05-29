#created, maintained by Soufiane
import pygame

# define your class
class Battle:
    
    # initializes a new instance of Battle class
    def __init__(self):
        pass
    
    #Define Battle function
    def _start_battle(self, groups, level):
        # Starts the battle loop using pygame
        # Set the game loop state
        battleState = True
        # Add an excepetion to catch errors and avoid the game to crashe
        try:
            # begin the game loop
            while(battleState): 
                # Loop trugh the built in event.get function of the pygame library
                # chceck if the game is quitting then exit
                # if mousebutton is clicked end the battle
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        battleState = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #remove element after it has collided
                        groups.remove(self.collidedItem)
                        level.pokemons.remove(self.collidedItem)
                        # Update groups
                        self.collidedItem.image = pygame.Surface((0,0))
                        groups.update()
                        battleState = False
                        self.run()
                # Create a font object
                font = pygame.font.SysFont("Arial", 30)
                
                # Render the text
                text_surface = font.render(f"Battle Begins!\nTrainer: Ash VS {self.collidedItem.name}\nclick on the screen to go back", True, (0, 0, 0))                # Position the text
                text_rect = text_surface.get_rect()
                text_rect.center = (400, 300)
                # Fill the background in white
                self.screen.fill("white")
                # draw it on the screen
                self.screen.blit(text_surface, text_rect)
           
                #update the display
                pygame.display.update()              
        except Exception as e:
            print(e)
    