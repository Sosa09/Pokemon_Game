import pygame
import sys

class Menu:
    def __init__(self, window_size):
        # Initialize Pygame
        pygame.init()

        # Set the window size
        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Game Menu")

        # Set colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BUTTON_COLOR = (0, 120, 200)
        self.BUTTON_HOVER_COLOR = (0, 150, 255)

        # Set fonts
        self.font = pygame.font.Font(None, 36)

        # Create buttons
        self.start_button = self.create_round_button("Start", self.BUTTON_COLOR, self.BUTTON_HOVER_COLOR)
        self.load_button = self.create_round_button("Load", self.BUTTON_COLOR, self.BUTTON_HOVER_COLOR)
        self.exit_button = self.create_round_button("Exit", self.BUTTON_COLOR, self.BUTTON_HOVER_COLOR)

        self.button_width, self.button_height = self.start_button.get_width(), self.start_button.get_height()

        # Position buttons
        self.button_spacing = 20  # Spacing between buttons
        self.button_x = (self.window_size[0] - (self.button_width * 3 + self.button_spacing * 2)) // 2
        self.button_y = 475

        self.start_pos = (self.button_x, self.button_y)
        self.load_pos = (self.button_x + self.button_width + self.button_spacing, self.button_y)
        self.exit_pos = (self.button_x + 2 * (self.button_width + self.button_spacing), self.button_y)

      
        # Load the background image
        background_image = pygame.image.load("images\pokemon.jpg")

        # Resize the background image to fit the display window
        background_image = pygame.transform.scale(background_image, (700, 500))

        # Blit the background image onto the screen
        self.screen.blit(background_image, (50, 50))      

    def create_round_button(self, text, color, hover_color):
        button_radius = 10  # Radius of the round button

        button_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, button_surface.get_rect(), border_radius=button_radius)

        text_render = self.font.render(text, True, self.WHITE)
        text_rect = text_render.get_rect(center=button_surface.get_rect().center)

        button_surface.blit(text_render, text_rect)

        return button_surface

    def draw_menu(self):

        # Draw buttons
        self.screen.blit(self.start_button, self.start_pos)
        self.screen.blit(self.load_button, self.load_pos)
        self.screen.blit(self.exit_button, self.exit_pos)

        # Update the display
        pygame.display.flip()
