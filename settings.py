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
        self.screen_height= 825
        self.resolution= (self.screen_width, self.screen_height)
        self.bg_color= (230,230,230)
        self.ship_speed = 3.0


        self.bullet_speed = 5.0
        self.bullet_width= 15
        self.bullet_height= 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 8

        self.alien_speed= 3.0


        