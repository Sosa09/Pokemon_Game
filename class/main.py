#created, maintained by Joris
import pygame
import sys
from menuscreen import MenuScreen
from settings import Settings
from intro import IntroVideo
from lab_oak import FirstGameScreen
from game import Game


def run_game():
    # Initialize Pygame
    pygame.init()

    # Set up the window by using Settings class
    screen_settings = Settings()
    screen_width = screen_settings.get_screen_width()
    screen_height = screen_settings.get_screen_height()

    # Set up the title
    pygame.display.set_caption("Pokemon")

    # Creating the screen itself
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Define colors
    BLACK = (0, 0, 0)

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

        # Check if the current screen is the game screen
        if isinstance(current_screen, FirstGameScreen): 
            # Check the current state of keyboard keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                current_screen.player_x -= current_screen.player_speed
            if keys[pygame.K_RIGHT]:
                current_screen.player_x += current_screen.player_speed
            if keys[pygame.K_UP]:
                current_screen.player_y -= current_screen.player_speed
            if keys[pygame.K_DOWN]:
                current_screen.player_y += current_screen.player_speed

if __name__ == "__main__":
    #IntroVideo().play()
    run_game()
