import pygame
import sys
from menu_screen import MenuScreen
from play_screen import PlayScreen
from options_screen import OptionsScreen
from scores_screen import ScoresScreen

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Screen Switching Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define screen indices
SCREEN_MENU = 0
SCREEN_PLAY = 1
SCREEN_OPTIONS = 2
SCREEN_SCORES = 3
SCREEN_EXIT = 4

# Set the current screen
current_screen = MenuScreen()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        current_screen = current_screen.handle_events(event)

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw the current screen
    current_screen.update()
    current_screen.draw(screen)

    # Update the display
    pygame.display.flip()





import pygame

class MenuScreen:
    def __init__(self):
        pass

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                return PlayScreen()
            elif event.key == pygame.K_2:
                return OptionsScreen()
            elif event.key == pygame.K_3:
                return ScoresScreen()
            elif event.key == pygame.K_4:
                pygame.quit()
                sys.exit()
        return self

    def update(self):
        pass

    def draw(self, screen):
        menu_text = "1: Play    2: Options    3: Scores    4: Exit"
        font = pygame.font.SysFont(None, 30)
        text = font.render(menu_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)






import pygame

class PlayScreen:
    def __init__(self):
        pass

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return MenuScreen()
        return self

    def update(self):
        pass

    def draw(self, screen):
        play_text = "Play Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(play_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
