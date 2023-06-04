#Created, Managed by Soufiane
import pygame, sys, random
from settings import *

# define your class
class Battle():
    CHOICE = ["Attack", "Sp Attack", "Defense", "Sp Def", "Recover", "Pokemons"]
    # initializes a new instance of Battle class
    def __init__(self):
        self.game = None
        self.ash = None
        self.ennemy = None
        self.opponent_x = -80
        self.opponent_y = 50
        self.battleStarted = False   
        
    #Define Battle function
    def go_to_battle(self,obj):
        # assign the pygame setting from the main game
        self.game = obj
        self.ennemy = self.game.collidedItem
        self.ash = self.game.level.player
        self._start_battle()      
    def _start_battle(self):
        # Set the game loop state
        battleState = True
        battlePresentationEnded = False
        # Create a font object
        font = pygame.font.SysFont("Arial", 30)
     
        text = f"Battle begins .... \nAsh VS {self.ennemy.name}\n\nPRESS SPACE TO SKIP"
        lines = text.split("\n")

        # Add an excepetion to catch errors and avoid the game to crashe
        try:
            # begin the game loop
            while battleState: 
                # Loop trugh the built in event.get function of the pygame library
                # chceck if the game is quitting then exit
                # if esc is pressed end the battle
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        battleState = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE: #skips the presentation process
                            battlePresentationEnded = True
                            self.ash.battle_x = 50
                            self.opponent_x = 1100
                        elif event.key ==pygame.K_ESCAPE: # or battle_ended:
                            self._go_to_map();       
                        elif event.key ==pygame.K_1:
                            self._battle(0)
                        elif event.key ==pygame.K_2:
                            self._battle(1)
                        elif event.key ==pygame.K_3:
                            self._battle(2)
                        elif event.key ==pygame.K_4:
                            self._battle(3)
                        elif event.key ==pygame.K_5:
                            self._battle(4)
                        elif event.key ==pygame.K_6:
                            self._battle(5)
                # # Fill the background in white
                self.game.screen.fill("white")
                if battlePresentationEnded == False:
                    if self.ash.battle_x != 50:
                        self.ash.battle_x = self.ash.battle_x - 3
                        self.opponent_x = self.opponent_x + 3
                    self._show_presentation_text(lines, font)
                    self.ash.show_trainer(pygame, self.game)
        
                else:
                    self.ash.pokemon_choice(pygame, self.game)
                    self._display_battle_options(font)
                    self.battleStarted = True;
                self._show_ennemy()
                self.game.clock.tick(60)
                
                #update the display
                pygame.display.update()         
        except Exception as e:
            print(e)            
    def _show_presentation_text(self, lines, font):
        #TEXT PROBLEM
        for i, line in enumerate(lines):    
            text_render = font.render(line,True,"black")
            text_rect = text_render.get_rect()
            text_rect.center = (600, 600 + i * 24)
            # draw it on the screen
            self.game.screen.blit(text_render, text_rect)
    def _show_ennemy(self):
        # load the opponent image
        opponent = self.ennemy.image

        opponent = pygame.transform.scale(opponent, (80, 80))
        self.game.screen.blit(opponent, (self.opponent_x, self.opponent_y))
        
        if(self.battleStarted):
            #health bar opponent
            pygame.draw.rect(self.game.screen, "black",(50,50,850,60),5, 1,1,1,1,1)
            pygame.draw.rect(self.game.screen, "blue", (60,60,830,40)) 
    def _display_battle_options(self, font):
        choicePositions = [(365, 500),(565, 500),(765, 500),(365, 600),(565, 600),(765, 600)]
        i = 0
        for c in self.CHOICE:
            rect = pygame.Rect(choicePositions[i][0],choicePositions[i][1], 150, 50)

            text_surface = font.render(f"{i + 1} {self.CHOICE[i]}", True, "White")
            text_rect = text_surface.get_rect(center=rect.center)
            # Blit the text surface onto the rectangle
            pygame.draw.rect(self.game.screen,"black",rect)
            self.game.screen.blit(text_surface, text_rect)
            i  = i + 1;
    def _battle(self,player_choice):
        ennemy_choice = random.randint(0,5)
        print(f"player choose {self.CHOICE[player_choice]}\nennemy choose {self.CHOICE[ennemy_choice]}");
    def _go_to_map(self):
        # #remove element after it has collided
        # self.game.groups.remove(self.ennemy)
        self.game.level.pokemons.remove(self.ennemy)
        # Update groups
        self.ennemy.image = pygame.Surface((0,0))
        self.game.groups.update()
        self.battleState = False
        self.battlePresentationEnded = False
        self.battleStarted = False
        self.ash.battle_x = 1280
        self.opponent_x = -80
        self.game.run()
