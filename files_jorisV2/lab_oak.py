import pygame
from screen import Screen
from settings import Settings

class FirstGameScreen(Screen):
    def __init__(self):
        super().__init__()
        # Load the player character image
        self.player_image = pygame.image.load("images/player.png")

        # Get the dimensions of the player image
        player_width = self.player_image.get_width()
        player_height = self.player_image.get_height()

        # Set the initial position of the player
        self.player_x = (800 - player_width) // 2
        self.player_y = (600 - player_height) 

        # Set the speed of the player movement. Its so low bc original pic is so small.
        self.player_speed = 100
    
    def draw(self, screen):
        # get screen settings from settings class
        screen_settings = Settings()
        width = screen_settings.get_screen_width()
        height = screen_settings.get_screen_height()

        # Load the background image
        background_image = pygame.image.load("files_joris\images\oak.jpg")
        
        # Scale the background image to fit the game screen
        background_image = pygame.transform.scale(background_image, (width, height))
        screen.blit(background_image, (0,0))

        # Draw the player image on the screen
        screen.blit(self.player_image, (self.player_x, self.player_y))


    def handle_events(self, event):
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_x += self.player_speed
        if keys[pygame.K_UP]:
            self.player_y -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_y += self.player_speed

        return self


















