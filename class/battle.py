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
        self.battlePresentationEnded = False  
        self.battleEnded = False  
         
    #Define Battle function
    def go_to_battle(self,obj):
        # assign the pygame setting from the main game
        self.game = obj
        self.ennemy = self.game.collidedItem
        self.ash = self.game.level.player
        text = ""
        self._start_battle()      
    def _start_battle(self):
        # Set the game loop state
        battleState = True
        # Create a font object
        font = pygame.font.SysFont("Arial", 30)
        # Add an excepetion to catch errors and avoid the game to crashe
        try:
            # begin the game loop
            while battleState: 
                # Loop trough the built in event.get function of the pygame library
                # chceck if the game is quitting then exit
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        battleState = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE: #skips the presentation process
                            self.battlePresentationEnded = True
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
                if self.battlePresentationEnded == False:
                    if self.ash.battle_x != 50:
                        self.ash.battle_x = self.ash.battle_x - 5
                        self.opponent_x = self.opponent_x + 5
                    else:
                        self.battlePresentationEnded = True
                        self.text = ""
                    self._show_presentation_text(font)
                    self.ash.show_trainer(pygame, self.game)
                    self._show_ennemy()
                
                else:
                    if self.battleEnded == False:
                        self.ash.pokemon_choice(pygame, self.game, self.ash.pokemons[0])
                        self._show_ennemy()
                        self._display_battle_options(font)
                        self._display_battle_text(font)
                        
                        
                    else:
                        self._display_end_text(font)
                
                self.game.clock.tick(60)
                
                #update the display
                pygame.display.update()         
        except Exception as e:
            print(e)            
    def _show_presentation_text(self,font, lines = []):
        #TEXT PROBLEM
        self.text = f"Battle begins .... \nAsh VS {self.ennemy.name}\n\nPRESS SPACE TO SKIP"

        lines = self.text.split("\n")
        for i, line in enumerate(lines):    
            text_render = font.render(line,True,"black")
            text_rect = text_render.get_rect()
            text_rect.center = (600, 600 + i * 24)
            # draw it on the screen
            self.game.screen.blit(text_render, text_rect)
    
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
            i  = i + 1
    def _display_end_text(self, font): 
        lines = self.text.split("\n")
        for i, line in enumerate(lines):    
            text_render = font.render(line,True,"black")
            text_rect = text_render.get_rect()
            text_rect.center = (640, 300 + i * 24)
            # draw it on the screen
            self.game.screen.blit(text_render, text_rect)
    def _display_battle_text(self,font):
            text_render = font.render(self.text,True,"black")
            text_rect = text_render.get_rect()
            text_rect.center = (640, 360)
            # draw it on the screen
            self.game.screen.blit(text_render, text_rect)
    def _battle(self,player_choice):
        ennemy_choice = random.randint(0,5)
        playerDamage = 0.0
        playerChoice = self.CHOICE[player_choice]
        ennemyChoice = self.CHOICE[ennemy_choice]
        ennemyDamage = 0.0
        # CHOICE = ["Attack", "Sp Attack", "Defense", "Sp Def", "Recover", "Pokemons"]
        
        #if player ATTACK and ENNEMY 0,1,2,3,4
        if player_choice == 0 and ennemy_choice == 0:
            playerDamage = self.ennemy.attack()
            ennemyDamage = self.ash.battlePokemon.attack()
        elif player_choice == 0 and ennemy_choice == 1:
            playerDamage = self.ennemy.special_attack()
            ennemyDamage = self.ash.battlePokemon.attack()    
        elif player_choice == 0 and ennemy_choice == 2:
            ennemyDamage = self.ash.battlePokemon.attack() - self.ennemy.defense()
        elif player_choice == 0 and ennemy_choice == 3:
            ennemyDamage = self.ash.battlePokemon.attack() - self.ennemy.special_defense()
        elif player_choice == 0 and ennemy_choice == 4:
            ennemyDamage = self.ash.battlePokemon.attack()
            self.ennemy.recover()
            
            
        #if player SP ATTACK and ENNEMY 0,1,2,3,4
        if player_choice == 1 and ennemy_choice == 0:
            playerDamage = self.ennemy.attack()
            ennemyDamage = self.ash.battlePokemon.special_attack()
        elif player_choice == 1 and ennemy_choice == 1:
            playerDamage = self.ennemy.special_attack()
            ennemyDamage = self.ash.battlePokemon.special_attack()   
        elif player_choice == 1 and ennemy_choice == 2:
            ennemyDamage = self.ash.battlePokemon.special_attack() - self.ennemy.defense()
        elif player_choice == 1 and ennemy_choice == 3:
            ennemyDamage = self.ash.battlePokemon.special_attack() - self.ennemy.special_defense()
        elif player_choice == 1 and ennemy_choice == 4:
            ennemyDamage = self.ash.battlePokemon.special_attack()
            self.ennemy.recover()
            
        #if player DEFENSE and ENNEMY 0,1,2,3,4  
        #defense if statements has been erased since defense against defense has no damage !        
        if player_choice == 2 and ennemy_choice == 0:
            playerDamage = self.ennemy.attack() - self.ash.battlePokemon.defense()
        elif player_choice == 2 and ennemy_choice == 1:
            playerDamage = self.ennemy.special_attack() - self.ash.battlePokemon.defense()
            ennemyDamage = self.ash.battlePokemon.attack()   
        elif player_choice == 2 and ennemy_choice == 4:
            self.ennemy.recover() 
            
        #if player SP DEFENSE and ENNEMY 0,1,2,3,4 
        #defense if statements has been erased since defense against defense has no damage !             
        if player_choice == 3 and ennemy_choice == 0:
            playerDamage = self.ennemy.attack()  - self.ash.battlePokemon.special_defense()
        elif player_choice == 3 and ennemy_choice == 1:
            playerDamage = self.ennemy.special_attack() - self.ash.battlePokemon.special_defense()
            ennemyDamage = self.ash.battlePokemon.attack()    
        elif player_choice == 3 and ennemy_choice == 4:
            self.ennemy.recover()
            
        #if player RECOVER and ENNEMY 0,1,2,3,4
        if player_choice == 4 and ennemy_choice == 0:
            playerDamage = self.ennemy.attack()
            self.ash.battlePokemon.recover()
        elif player_choice == 4 and ennemy_choice == 1:
            playerDamage = self.ennemy.special_attack()
            self.ash.battlePokemon.recover()    
        elif player_choice == 4 and ennemy_choice == 2:
            self.ash.battlePokemon.recover()
        elif player_choice == 4 and ennemy_choice == 3:
            self.ash.battlePokemon.recover()
        elif player_choice == 4 and ennemy_choice == 4:
            self.ash.battlePokemon.recover()
            self.ennemy.recover()
        
        #if player SWAP POKEMON and ENNEMY 0,1,2,3,4
        elif player_choice == 5 and ennemy_choice == 0:
            self.swap_pokemon()
            playerDamage = self.ennemy.special_attack()

        elif player_choice == 5 and ennemy_choice == 1:
            self.swap_pokemon()
            playerDamage = self.ennemy.special_attack()

        elif player_choice == 5 and ennemy_choice == 2:
            self.swap_pokemon()
            playerDamage = self.ennemy.special_attack()
    
        elif player_choice == 5 and ennemy_choice == 3:
            self.swap_pokemon()
            playerDamage = self.ennemy.special_attack()
  
        elif player_choice == 5 and ennemy_choice == 4:
            self.swap_pokemon()
            playerDamage = self.ennemy.special_attack()
            
        self.text = f"Ennemy's choice: {ennemyChoice} caused {playerDamage}\n\n\nplayer's choice {playerChoice} caused {ennemyDamage}"
        
        #Player pokemon update hp and healthbar
        self.ash.battlePokemon.set_healthBarValue(playerDamage*4)
        #Ennemy update hp and healthbar
        self.ennemy.set_healthBarValue(ennemyDamage*4)
        
        #Check if ennemy or player is on 0 or lower
        if(self.ennemy.get_healthBarValue() <= 0):
            self.battleEnded = True 
            self.text = "Great you won ! Press ESC to go back to the map"
        elif(self.ash.battlePokemon.get_healthBarValue() <= 0):
            self.battleEnded = True 
            self.text = "Damn you lost! Press ESC to go back to the map"
        
    def _go_to_map(self):
        # #remove element after it has collided
        # self.game.groups.remove(self.ennemy)
        self.game.level.pokemons.remove(self.ennemy)
        # Update groups
        self.ennemy.image = pygame.Surface((0,0))
        self.game.groups.update()
        self.battleState = False
        self.battlePresentationEnded = False
        self.text = ""
        self.ash.battle_x = 1280
        self.opponent_x = -80
        self.game.run()
    def _show_ennemy(self):
        # load the opponent image
        opponent = self.ennemy.image

        opponent = pygame.transform.scale(opponent, (80, 80))
        self.game.screen.blit(opponent, (self.opponent_x, self.opponent_y))
        
        if(self.battlePresentationEnded):
            #health bar opponent
            pygame.draw.rect(self.game.screen, "black",(50,50,850,60),5, 1,1,1,1,1)
            pygame.draw.rect(self.game.screen, "blue", (60,60,self.ennemy.get_healthBarValue(),40)) 