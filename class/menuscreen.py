import pygame
import sys
from screen import Screen
from button import Button
from settings import Settings
from intro import IntroVideo
from lab_oak import FirstGameScreen
from game import Game

# Menu screen class
class MenuScreen(Screen):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = (255, 255, 255)
        self.button_color = (50, 50, 50)
        self.hover_color = (100, 100, 100)
        self.create_buttons()

    def create_buttons(self):
        # get screen settings from settings class
        screen_settings = Settings()
        width = screen_settings.get_screen_width()
        height = screen_settings.get_screen_height()

        # Position buttons
        button_spacing = 20  # Spacing between buttons
        button_width = 200
        button_height = 50
        total_buttons = 4

        # starting possition
        x = (width - (button_width * total_buttons + button_spacing * total_buttons)) // 2
        y = (height - 100) 

        button_texts = ["Play Oak's Lab", "Play Wilderness", "Exit"]
        for i, text in enumerate(button_texts):
            button_x = x + ((i * button_width) * 1.15)
            button = Button(button_x, y, button_width, button_height, text,
                            self.font, self.text_color, self.button_color, self.hover_color)
            self.buttons.append(button)

    def handle_events(self, event):
        for button in self.buttons:
            if button.handle_event(event):
                button_text = button.text.lower()
                if button_text == "play oak's lab":
                    return FirstGameScreen().run()
                elif button_text == "play wilderness":
                    return Game().run()
                elif button_text == "exit":
                    pygame.quit()
                    sys.exit()
        return self

    def update(self):
        pass

    def draw(self, screen):
        screen_settings = Settings()
        width = screen_settings.get_screen_width()
        height = screen_settings.get_screen_height()

        # Load the background image
        background_image = pygame.image.load("images\pokemon.jpg")

        # Resize the background image to fit the display window
        background_image = pygame.transform.scale(background_image, (width - 90, height - 90))

        # Blit the background image onto the screen
        screen.blit(background_image, (40, 40)) 

        for button in self.buttons:
            button.draw(screen)
