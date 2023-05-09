import pygame
import sys
from menu import Menu

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if menu.start_pos[0] <= mouse_pos[0] <= menu.start_pos[0] + menu.button_width and \
                menu.start_pos[1] <= mouse_pos[1] <= menu.start_pos[1] + menu.button_height:
                    print("Starting the game...")
                    # Add your game start code here
                elif menu.load_pos[0] <= mouse_pos[0] <= menu.load_pos[0] + menu.button_width and \
                    menu.load_pos[1] <= mouse_pos[1] <= menu.load_pos[1] + menu.button_height:
                    print("Loading the game...")
                    # Add your game load code here
                elif menu.exit_pos[0] <= mouse_pos[0] <= menu.exit_pos[0] + menu.button_width and \
                    menu.exit_pos[1] <= mouse_pos[1] <= menu.exit_pos[1] + menu.button_height:
                    print("Exiting the game...")
                    pygame.quit()
                    sys.exit()

        # Draw the menu
        menu.draw_menu()

if __name__ == "__main__":
    pygame.init()
    run_game()
