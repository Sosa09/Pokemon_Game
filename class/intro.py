#created, maintained by Joris
import pygame
from moviepy.editor import VideoFileClip
from settings import Settings

# To install MoviePy:
# pip install moviepy

class IntroVideo:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.video_path = "images\Intro\pokemon_intro.mp4"

    def play(self):
        # Initialize Pygame
        pygame.init()

        screen_settings = Settings()
        width = screen_settings.get_screen_width()
        height = screen_settings.get_screen_height()
        
        # Create the screen
        pygame.display.set_mode((width, height))
        pygame.display.set_caption("Intro Video")

        # Load the MP4 video clip
        video = VideoFileClip(self.video_path)

        # Resize the video clip
        video = video.resize((width, height))

        # Play the video
        video.preview(fps=30, audio_fps=video.audio.fps, audio=True)







