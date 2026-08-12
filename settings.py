"""
Alien Invasion
Stuti Pathak
This class is to store all the settings of the game, including screen width, height, background color, and speed for the various objects, and the size of the objects (bullets, ship, aliens).
Starter code: From Python Crash Course book and Python Programming lectures.
7/27/2026
"""
class Settings:
    def __init__(self):
        self.screen_width= 1200
        self.screen_height= 825
        self.resolution= (self.screen_width, self.screen_height)
        self.bg_color= (230,230,230)
        


       
        self.bullet_width=15
        self.bullet_height= 300
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 8

        self.fleet_drop_speed= 8
    

        self.speedup_scale= 2 #1.1
        self.ship_lives=3

        self.intialize_dynamic_settings()

    def intialize_dynamic_settings(self):
        self.ship_speed = 10.0
        self.alien_speed= 1.0
        self.bullet_speed = 5.0
        self.alien_points=50
        
        self.fleet_direction= 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed*= self.speedup_scale
        self.bullet_speed*= self.speedup_scale
        


        