#created, maintained by Joris
import pygame
import sys
from button import Button
from level_lab_oak import LevelLabOak
from settings_lab_oak import *

class FirstGameScreen():
    def __init__(self):
        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Oak\'s lab')
        self.clock = pygame.time.Clock()
        self.level = LevelLabOak()
        self.groups = pygame.sprite.Group()
        self.groups.add(self.level.pokemons)
        
        #background
        self.draw(self.screen)

        # going to add a button to pause the game (added by Joris)  
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.hover_color = (100, 100, 100)
        self.new_button = Button(100, 50, 200, 50, "Pause", self.font, self.text_color, self.button_color, self.hover_color)


            
        # Load the player character image
        self.player_image = pygame.image.load("images\player.png")

    def run(self):
        running = True
        event = None  # Add this line to define a default value for event
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.K_ESCAPE:
                          # Create a font object
                    font = pygame.font.SysFont("Arial", 30)
                    text_surface = font.render(f"Battle Begins!\nTrainer: Ash ", True, (0, 0, 0))                # Position the text
                    #text_rect = text_surface.get_rect()
                    #text_rect.center = (400, 300)
                
                
            
            # Handle button events
            self.new_button.handle_event(event)
            if self.new_button.handle_event(event):
                running = not running

            # check if the player collide with on of the elements
            for x in self.level.pokemons: 
                if pygame.sprite.collide_rect(self.level.player, x):
                    running = False
                    self.collidedItem = x
                    self._start_battle_loop()
                    #background
            self.draw(self.screen)
            self.level.run()
            
            self.new_button.draw(self.screen) # added to show button on the screen (Added by Joris)
            
            pygame.display.update()
            self.clock.tick(FPS)
            
    def _start_battle_loop(self):
          # begin battle
        battleState = True
        try:
            while(battleState): 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        battleState = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #remove element after it has collided
                        self.groups.remove(self.collidedItem)
                        self.level.pokemons.remove(self.collidedItem)
                        # Update groups
                        self.collidedItem.image = pygame.Surface((10,10))
                        self.groups.update()
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



    

    def draw(self, screen):
        # Load the background image
        background_image = pygame.image.load("images\oak.png")
        
        # Scale the background image to fit the game screen
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGTH))
        screen.blit(background_image, (0, 0))

    