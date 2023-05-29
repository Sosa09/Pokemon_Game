import pygame

class FirstGameScreen:
    def __init__(self, window_size):
        # Initialize Pygame
        pygame.init()
        # Set the window size
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Oak's Lab")

        # Load the player character image
        self.player_image = pygame.image.load("images/player.png")

        # Get the dimensions of the player image
        player_width = self.player_image.get_width()
        player_height = self.player_image.get_height()

        # Set the initial position of the player
        self.player_x = (800 - player_width) // 2
        self.player_y = (600 - player_height) 

        # Set the speed of the player movement. Its so low bc original pic is so small.
        self.player_speed = 10
    
    def load_background(self):
        # Load the background image
        self.background_image = pygame.image.load("files_joris\images\oak.jpg")
        # Scale the background image to fit the game screen
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        # Create a separate surface for the background
        self.background_surface = pygame.Surface((800,600))
        self.background_surface.blit(self.background_image, (0, 0))

    def game_loop(self):
        running = True
        while running:
            self.load_background()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

                # Update the game display
                self.screen.blit(self.background_surface, (0, 0))
                self.screen.blit(self.player_image, (self.player_x, self.player_y))
                pygame.display.update()

        # Quit the game
        pygame.quit()




#if __name__ == "__main__":
#    test = FirstGameScreen((800,600))
#    test.game_loop()
#    test.load_player()















