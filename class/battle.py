#Created, Managed by Soufiane
import pygame, sys
from settings import *

# define your class
class Battle():
    
    # initializes a new instance of Battle class
    def __init__(self):
        self.game = None
        self.ash = None
        self.ennemy = None
        
    
    #Define Battle function
    def go_to_battle(self,obj):
        # assign the pygame setting from the main game
        self.game = obj
        self.ennemy = self.game.collidedItem
        self._start_battle()
        
    def _start_battle(self):
        # Set the game loop state
        battleState = True
  
        # Create a font object
        font = pygame.font.SysFont("Arial", 30)
        #load the text
        text = f"Battle Begins!\nAsh VS {self.ennemy.name}"
        lines = text.split("\n")
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
                        pygame.quit()
                        sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                        #remove element after it has collided
                        obj.groups.remove(obj.collidedItem)
                        obj.level.pokemons.remove(obj.collidedItem)
                        # Update groups
                        obj.collidedItem.image = pygame.Surface((0,0))
                        obj.groups.update()
                        battleState = False
                        obj.run()
        
                
                # Render the text
                for i, line in enumerate(lines):
                    text_surface = font.render(line, True, (255, 255, 255),"black") # Position the text
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (50, 50 + i * 12)
                    # draw it on the screen
                    self.game.screen.blit(text_surface, text_rect)
                # # Fill the background in white
                self.game.screen.fill("white")
                
                self._show_trainers_pokemon()
                self._show_ennemy()
                self.game.clock.tick(60)
                
                #update the display
                pygame.display.update()    
       
        except Exception as e:
            print(e)
    
    # Display Battle elements dynamically (Player vs Opponent) 
    def _show_trainer(self):
        
        # ASH botto left corner
        player_width = 50
        player_height = 50
        player_color = (25,3,5)
        player_x = 50
        player_y = 400
    
    def _show_trainers_pokemon(self):
        #load the trainer image
        image = pygame.image.load("Images/Trainers/ashBattle.png")
        image = pygame.transform.scale(image, (100, 100))
        self.game.screen.blit(image, (50, 380))
        
        #health bar trainer
        pygame.draw.rect(self.game.screen, "black",(200,400,850,60),5, 1,1,1,1,1)
        pygame.draw.rect(self.game.screen, "red", (210,410,830,40))
        

    def _show_ennemy(self):
        # load the opponent image
        opponent = pygame.image.load(f"{self.game.collidedItem.path}")
        opponent = pygame.transform.scale(opponent, (80, 80))
        self.game.screen.blit(opponent, (1000, 50))
        
        #health bar opponent
        pygame.draw.rect(self.game.screen, "black",(50,50,850,60),5, 1,1,1,1,1)
        pygame.draw.rect(self.game.screen, "blue", (60,60,830,40))
    def _display_battle_options(self):
        pass
    def _multiple_choice_battle(self):
        pass
    # load all elements that will be displayed on the battle screen
    def _load_assets(self):
        pass