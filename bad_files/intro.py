import pygame
import sys
from screen import Screen
from settings import Settings
from moviepy.editor import VideoFileClip
from lab_oak import FirstGameScreen

# To install MoviePy:
# pip install moviepy

# Custom event ID for video end
VIDEO_END_EVENT = pygame.USEREVENT + 1

class IntroVideo(Screen):
    def __init__(self):
        super().__init__()
        self.video_path = "files_jorisV2\images\pokemon_intro.mp4"
        self.clock = pygame.time.Clock()
        self.movie = None

        # Set up the event for video end
        pygame.mixer.music.set_endevent(VIDEO_END_EVENT)

    def play(self):
        # get screen settings from settings class
        screen_settings = Settings()
        width = screen_settings.get_screen_width()
        height = screen_settings.get_screen_height()

        # Load the MP4 video clip
        video = VideoFileClip(self.video_path)
        # Resize the video clip
        video = video.resize((width, height))

        # Play the video
        video.preview(fps=30, audio_fps=video.audio.fps, audio=True)


    # Handle video end event
    def handle_events(self, event):

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == VIDEO_END_EVENT:
            print("Video ended!")
            return FirstGameScreen()
    

    def update(self):
        pass

    def draw(self, screen):
        # Draw elements here
        pass


