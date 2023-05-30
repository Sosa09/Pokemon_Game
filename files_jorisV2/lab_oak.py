#created, maintained by Joris
import pygame
from screen import Screen
from settings import Settings

class FirstGameScreen(Screen):
    def __init__(self):
        super().__init__()
        # Load the player character image
        self.player_image = pygame.image.load("images\player.png")

        # get screen settings from settings class
        screen_settings = Settings()
        self.width = screen_settings.get_screen_width()
        self.height = screen_settings.get_screen_height()

        # Get the dimensions of the player image
        self.player_width = self.player_image.get_width()
        self.player_height = self.player_image.get_height()

        # Set the initial position of the player
        self.player_x = (self.width - self.player_width) // 2
        self.player_y = (self.height - self.player_height)

        # Variables to store previous player position
        self.previous_player_x = self.player_x
        self.previous_player_y = self.player_y

        # List of obstacles
        self.obstacles = []

        # Define obstacles
        obstacle1 = pygame.Rect(788, 230, 287, 70)
        self.obstacles.append(obstacle1)

        # Color for obstacle visualization
        self.obstacle_color = (255, 0, 0)  # Red

        # Set the speed of the player movement
        self.player_speed = 5

    def draw(self, screen):
        # Load the background image
        background_image = pygame.image.load("images\oak.png")
        
        # Scale the background image to fit the game screen
        background_image = pygame.transform.scale(background_image, (self.width, self.height))
        screen.blit(background_image, (0, 0))

        # Draw the player image on the screen
        screen.blit(self.player_image, (self.player_x, self.player_y))

        # Drawing a rectangle over the player for collision detection
        player_rect = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)

        # Draw the obstacle rectangles and check for collision
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, self.obstacle_color, obstacle)
            if player_rect.colliderect(obstacle):
                # Prevent player movement or move the player back to the previous position
                self.player_x = self.previous_player_x
                self.player_y = self.previous_player_y

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.previous_player_x = self.player_x  # Store the previous position
                self.player_x -= self.player_speed
            elif event.key == pygame.K_RIGHT:
                self.previous_player_x = self.player_x  # Store the previous position
                self.player_x += self.player_speed
            elif event.key == pygame.K_UP:
                self.previous_player_y = self.player_y  # Store the previous position
                self.player_y -= self.player_speed
            elif event.key == pygame.K_DOWN:
                self.previous_player_y = self.player_y  # Store the previous position
                self.player_y += self.player_speed
        
        # here to calculate the obstacles
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Handle left mouse button click
                print("Left mouse button clicked at", event.pos)
            elif event.button == 3:  # Right mouse button
                # Handle right mouse button click
                print("Right mouse button clicked at", event.pos)

        return self
