import pygame, sys
from settings import *
from level import Level

class Game:

    def __init__(self):
        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('POKEMON SYNTRA')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.groups = pygame.sprite.Group()
        self.groups.add(self.level.pokemons)
        
   
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.K_ESCAPE:
                          # Create a font object
                    font = pygame.font.SysFont("Arial", 30)
                    text_surface = font.render(f"Battle Begins!\nTrainer: Ash ", True, (0, 0, 0))                # Position the text
                    text_rect = text_surface.get_rect()
                    text_rect.center = (400, 300)
            # check if the player collide with on of the elements
            for x in self.level.pokemons: 
                if pygame.sprite.collide_rect(self.level.player, x):
                    running = False
                    self.collidedItem = x
                    self._start_battle_loop()
            self.screen.fill('chartreuse4')
            self.level.run()
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
if __name__=='__main__':
    game = Game()
    game.run()