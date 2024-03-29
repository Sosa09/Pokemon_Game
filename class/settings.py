# Created and managed by Tanguy
WIDTH    = 1280 
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
 
WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','z',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','g','1','g','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ','g','g','g','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ','p','x',' ',' ',' ',' ',' ',' ',' ',' ','p','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ','g','g','g',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ','5','x',' ',' ',' ','g','2','g',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ','g','g','g',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','g','g',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','g','g','g','x'],
['x',' ','3','g',' ',' ',' ',' ',' ','p',' ',' ',' ',' ',' ',' ','g','4','g','x'],
['x',' ','g','g',' ','b',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','g','g','g','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]


# added by Joris (can be refactored if i got time)
class Settings():
    def __init__(self):
        #screen settings
        self.screen_width = 1280
        self.screen_height = 720
    
    def get_screen_width(self):
       return self.screen_width
    
    def get_screen_height(self):
       return self.screen_height