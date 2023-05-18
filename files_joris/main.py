import pygame
import sys
from intro import IntroVideo
from main_menu import Menu

def run_game():
    # Set the window size
    window_size = (800, 600)

    # Create a menu instance
    menu = Menu(window_size)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                menu.handle_event(event)  # calls then menu event

        # Draw the menu
        menu.draw_menu()

if __name__ == "__main__":
    pygame.init()
    intro = IntroVideo("files_joris\images\pokemon_intro.mp4", 800, 600)
    intro.play(163) # In seconds
    run_game()
