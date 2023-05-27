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

# Define screen indices
SCREEN_MENU = 0
SCREEN_PLAY = 1
SCREEN_OPTIONS = 2
SCREEN_SCORES = 3
SCREEN_EXIT = 4

# Set the current screen
current_screen = SCREEN_MENU

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if current_screen == SCREEN_MENU:
                if event.key == pygame.K_1:
                    current_screen = SCREEN_PLAY
                elif event.key == pygame.K_2:
                    current_screen = SCREEN_OPTIONS
                elif event.key == pygame.K_3:
                    current_screen = SCREEN_SCORES
                elif event.key == pygame.K_4:
                    current_screen = SCREEN_EXIT
            elif current_screen == SCREEN_PLAY:
                # Handle input for the play screen
                if event.key == pygame.K_ESCAPE:
                    current_screen = SCREEN_MENU
            elif current_screen == SCREEN_OPTIONS:
                # Handle input for the options screen
                if event.key == pygame.K_ESCAPE:
                    current_screen = SCREEN_MENU
            elif current_screen == SCREEN_SCORES:
                # Handle input for the scores screen
                if event.key == pygame.K_ESCAPE:
                    current_screen = SCREEN_MENU
            elif current_screen == SCREEN_EXIT:
                pygame.quit()
                sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw content based on the current screen
    if current_screen == SCREEN_MENU:
        # Draw menu screen content
        menu_text = "1: Play    2: Options    3: Scores    4: Exit"
        font = pygame.font.SysFont(None, 30)
        text = font.render(menu_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    elif current_screen == SCREEN_PLAY:
        # Draw play screen content
        play_text = "Play Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(play_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    elif current_screen == SCREEN_OPTIONS:
        # Draw options screen content
        options_text = "Options Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(options_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    elif current_screen == SCREEN_SCORES:
        # Draw scores screen content
        scores_text = "Scores Screen (Press ESC to return to menu)"
        font = pygame.font.SysFont(None, 30)
        text = font.render(scores_text, True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()