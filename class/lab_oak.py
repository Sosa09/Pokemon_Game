#created, maintained by Joris
import json
import pygame
import sys
from lab_oak_level import LevelLabOak
from lab_oak_settings import *



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

            
        # Load the player character image
        self.player_image = pygame.image.load("images\player.png")

        # Set box dimensions
        self.BOX_WIDTH = 200
        self.BOX_HEIGHT = 250
        self.box_color = (128, 128, 128)  # Gray

        # Set text parameters
        self.FONT_SIZE = 18
        self.FONT_COLOR = (0, 0, 0)  # Black

        # Load box image
        self.box_image = pygame.Surface((self.BOX_WIDTH, self.BOX_HEIGHT))

        # Create a font object
        self.font = pygame.font.Font(None, self.FONT_SIZE)

    def run(self):

        running = True
        event = None  # Add this line to define a default value for event
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                

            #Check if the player collides with any elements
            for pokemon in self.level.pokemons:
                if pygame.sprite.collide_rect(self.level.player, pokemon):
                    self.collided_item = pokemon
                    self.display_info(pokemon.name, pokemon._load_image())  # Display Pokémon info
                    pygame.display.update()
                    

            for exi in self.level.exit:        
                if pygame.sprite.collide_rect(self.level.player, exi):
                    if self.level.player.pokemons.count != 0:
                        pygame.quit()
                        sys.exit
                    
            self.draw(self.screen)
            self.level.run()
            
            pygame.display.update()
            self.clock.tick(FPS)

    def load_pokemon_info_from_json(self, pokemon_name):
        with open('Database\pokemons_db.json') as f:
            data = json.load(f)
            info = data["pokemons"]
            for pokemon in info:
                if pokemon['name'] == pokemon_name:
                    return pokemon
        return None

    
    def display_info(self, pokemon_name, image):

                # Check if the 'T' key was pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            
            if len(self.level.player.pokemons) < 1:
                self.level.player.pokemons.append(self.collided_item)
                print(self.level.player.pokemons)
                self.selected_pokemon = self.collided_item
                self.groups.remove(self.collided_item)
                self.level.pokemons.remove(self.collided_item)
                self.groups.update()
            pygame.display.update()

        # Load Pokémon information from JSON file
        pokemon_info = self.load_pokemon_info_from_json(pokemon_name)

        # Prepare the stats string
        stats = f"HP: {pokemon_info['hp']}  \n" \
                f"Attack: {pokemon_info['at']}  \n" \
                f"Defense: {pokemon_info['df']}  \n" \
                f"Sp. Attack: {pokemon_info['spa']}  \n" \
                f"Sp. Defense: {pokemon_info['spdef']}  \n" \
                f"Speed: {pokemon_info['spd']}   \n " \
                f"\n" \
                f"Press 't' to take the pokemon"
        
        # Render text surfaces
        name_surface = self.font.render("Name: " + pokemon_info["name"], True, self.FONT_COLOR)
        
        stats_lines = stats.split('\n')  # Split the stats string into separate lines
        
        # Render each line of stats as a separate surface
        stats_surfaces = []
        for line in stats_lines:
            stats_surfaces.append(self.font.render(line, True, self.FONT_COLOR))

        # Render text surfaces
        name_surface = self.font.render("Name: " + pokemon_info["name"], True, self.FONT_COLOR)
        stats_surface = self.font.render(stats, True, self.FONT_COLOR)

        # Set text positions within the box
        name_position = (700, 225)  # Fixed position for name

        # Blit the box onto the screen
        self.screen.blit(self.box_image, (700, 150))  # Fixed position for the box

        # Clear the box image and fill it with the box color
        self.box_image.fill(self.box_color)

        # Blit the text surfaces onto the screen
        self.screen.blit(name_surface, name_position)

        # Draw the stats surfaces onto the screen
        stats_y = 250  # Starting position for the stats lines
        for surface in stats_surfaces:
            self.screen.blit(surface, (700, stats_y))
            stats_y += surface.get_height()  # Increase the vertical position

        # Blit the Pokémon image
        self.screen.blit(image, (700, 150))  # Fixed position for the image  







        
            
    # def _start_battle_loop(self):
    #       # begin battle
    #     battleState = True
    #     try:
    #         while(battleState): 
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     battleState = False
    #                 if event.type == pygame.MOUSEBUTTONDOWN:
    #                     #remove element after it has collided
    #                     self.groups.remove(self.collidedItem)
    #                     self.level.pokemons.remove(self.collidedItem)
    #                     # Update groups
    #                     self.collidedItem.image = pygame.Surface((10,10))
    #                     #self.groups.update()
    #                     battleState = False
    #                     self.run()
    #             # Create a font object
    #             font = pygame.font.SysFont("Arial", 30)

    #             # Render the text
    #             text_surface = font.render(f"Battle Begins!\nTrainer: Ash VS {self.collidedItem.name}\nclick on the screen to go back", True, (0, 0, 0))                # Position the text
    #             text_rect = text_surface.get_rect()
    #             text_rect.center = (400, 300)
    #             # Fill the background in white
    #             self.screen.fill("white")
    #             # draw it on the screen
    #             self.screen.blit(text_surface, text_rect)
           
    #             #update the display
    #             pygame.display.update()
            
                  
    #     except Exception as e:
    #         print(e)


    def update(self):
        # Update the menu screen state
        pass
    

    def draw(self, screen):
        # Load the background image
        background_image = pygame.image.load("images\oak.png")
        
        # Scale the background image to fit the game screen
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGTH))
        screen.blit(background_image, (0, 0))

