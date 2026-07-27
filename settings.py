"""
Alien Invasion
Stuti Pathak
This class is to store all the settings of the game, including screen width, height, background color, and speed for the various objects, and the size of the objects (bullets, ship, aliens).
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""
class Settings:
    def __init__(self):
        self.screen_width= 1200
        self.screen_height= 800
        self.resolution= (self.screen_width, self.screen_height)
        