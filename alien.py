"""
Alien Invasion
Stuti Pathak
Purpose: This is the class designed for the alien ship fleet by using sprite class of pygame. The alien ship will enter the screen from the left side, and move toward the ship on the right side of the screen.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
8/3/2026
"""

import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()


        self.screen= ai_game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.image= pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()


        self.rect.x= self.rect.width 
        #this will put the aliens on the left side of the screen
        self.rect.y= self.rect.height

        self.settings= ai_game.settings

    def update(self):
     """Moves the alien down the screen"""
     self.rect.y+= self.settings.alien_speed* self.settings.fleet_direction

    def check_edges(self):
       """Will return true if the alien is at the edge of the screen"""
       screen_rect= self.screen.get_rect()
       return(self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)



        
