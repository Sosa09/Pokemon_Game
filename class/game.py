import pygame, sys, time, copy
from pokeball import Pokeball
from potion import Potion
from settings import *
from level import Level
from battle import Battle
from pokemon import *
class Game:

    def __init__(self):
        #de Basics
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('POKEMON SYNTRA')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.itemCollided = False
        self.groups = pygame.sprite.Group()
        self.text = ""
        self.groups.add(self.level.pokemons)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                        
            # check for collisions
            self.collision_detection()
            self.screen.fill('chartreuse4')
            self.level.run()
            if self.itemCollided:    
                self._show_collidedItem()
                pygame.display.update()
                time.sleep(0.5)
                self.itemCollided = False
                self.text = ""  
            pygame.display.update()
            self.clock.tick(FPS)
    def _show_collidedItem(self):
        font = pygame.font.SysFont("Arial", 72, True)
        text_surface = font.render(self.text, True, "white")
        text_render = text_surface.get_rect()
        text_render.center = (200, 200)
        self.screen.blit(text_surface, text_render)
        
    def collision_detection(self):
        #the colission detection works by looping through all the pokemons available on the maps coliding with the actual Player
        for x in self.level.pokemons: 
            if pygame.sprite.collide_rect(self.level.player, x):
                #collidedItem contains the object with
                battle = Battle()
                self.collidedItem = x
                battle.go_to_battle(self)
        for item in self.level.items:
            if pygame.sprite.collide_rect(self.level.player, item):
                self.itemCollided = True
                self.text = f"+1 {item.name}"
                self.level.player.bag.append(copy.copy(item))
                self.level.items.remove(item)
                self.groups.remove(item)
                item.image = pygame.Surface((0,0))
                if type(item) == Pokeball:
                    name = self.level.list_pokemons[len(self.level.list_pokemons) -1]
                    self.text = f"+1 {item.name}; Congratulations you found a {name.name}";
                    self.level.player.pokemons.append(self.level.list_pokemons[len(self.level.list_pokemons) -1])
                
                
        #this collision is triggered if a pokeball or posion has been found
        #code here.

if __name__=='__main__':
    game = Game()
    game.run()