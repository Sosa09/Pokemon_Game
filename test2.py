import pygame
import sys

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

# Base screen class
class Screen:
    def __init__(self):
        pass

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

# Menu screen class
class MenuScreen(Screen):
    def __init__(self):
        super().__init__()

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

    def draw(self, screen):
        menu_text = "1: Play    2: Options    3: Scores    4: Exit"
        font = pygame.font.SysFont(None, 30)
        text = font.render(menu_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

# Play screen class
class PlayScreen(Screen):
    def __init__(self):
        super().__init__()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return MenuScreen()
        return self

    def draw(self, screen):
        play_text = "Play Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(play_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

# Options screen class
class OptionsScreen(Screen):
    def __init__(self):
        super().__init__()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return MenuScreen()
        return self

    def draw(self, screen):
        options_text = "Options Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(options_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

# Scores screen class
class ScoresScreen(Screen):
    def __init__(self):
        super().__init__()

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return MenuScreen()
        return self

    def draw(self, screen):
        scores_text = "Scores Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(scores_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

# Set the initial screen
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
