import pygame
import sys
from intro import IntroVideo
from main_menu import Menu
from lab_oak import FirstGameScreen

def run_game():
    # Set the window size
    window_size = (800, 600)

    # Create a menu instance
    menu = Menu(window_size)
    running_menu = True

    # Create first Game map instance
    lab = FirstGameScreen(window_size)
    running_lab_oak = False


    running_pause_button = False
    running_open_world = False
    running_battle_mode = False





    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif running_menu == True:
                menu.handle_event(event)  # calls then menu event

            elif running_lab_oak == True:
                lab.game_loop()
                running_menu = False


        if running_menu == True:
            # Draw the menu
            menu.draw_menu()

        elif running_lab_oak == True:
            # load player
            lab.load_player()





if __name__ == "__main__":
    pygame.init()
    intro = IntroVideo("files_joris\images\pokemon_intro.mp4", 800, 600)
    intro.play(163) # In seconds
    run_game()
