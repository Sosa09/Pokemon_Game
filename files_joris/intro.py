import pygame
import sys
from moviepy.editor import VideoFileClip

# To install MoviePy:
# pip install moviepy

class IntroVideo:
    def __init__(self, video_path, screen_width, screen_height):
        self.video_path = video_path
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = pygame.time.Clock()

    def play(self, video_duration=None):
        # Initialize Pygame
        pygame.init()

        # Create the screen
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Intro Video")

        # Load the MP4 video clip
        video = VideoFileClip(self.video_path)

        # Resize the video clip
        video = video.resize((self.screen_width, self.screen_height))

        # Play the video
        video.preview(fps=30, audio_fps=video.audio.fps, audio=True)

        # Set the video duration
        if video_duration is not None:
            video = video.subclip(0, video_duration)

# zou graag nog iets adden om met key event te kunnen stoppen
# en om alles in zelfde screen te krijgen



