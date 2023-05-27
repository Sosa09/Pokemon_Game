import pygame

class FirstGameScreen:
    def __init__(self, window_size):
        # Initialize Pygame
        pygame.init()
        # Set the window size
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Oak's Lab")
    ()
    def load_background(self):
        # Load the background image
        self.background_image = pygame.image.load("files_joris\images\oak.jpg")
        # Scale the background image to fit the game screen
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        # Create a separate surface for the background
        background_surface = pygame.Surface((800,600))
        background_surface.blit(self.background_image, (0, 0))

    def load_player(self):
        # Load the player character image
        player_image = pygame.image.load("images/player.png")

        # Get the dimensions of the player image
        player_width = player_image.get_width()
        player_height = player_image.get_height()

        # Set the initial position of the player
        player_x = (800 - player_width) // 2
        player_y = (600 - player_height) 

        # Set the speed of the player movement. Its so low bc original pic is so small.
        self.player_speed = 0.5

    def game_loop(self):
        running = True
        while running:
            self.load_background()
            self.load_player()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Player movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    player_x -= self.player_speed
                if keys[pygame.K_RIGHT]:
                    player_x += self.player_speed
                if keys[pygame.K_UP]:
                    player_y -= self.player_speed
                if keys[pygame.K_DOWN]:
                    player_y += self.player_speed

                # Update the game display
                self.screen.blit(self.background_surface, (0, 0))
                self.screen.blit(player_image, (player_x, player_y))
                pygame.display.update()

            # Quit the game
            pygame.quit()




















