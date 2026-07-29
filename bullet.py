"""
Alien Invasion
Stuti Pathak
This class is to create the sprites for the bullet of the game, and postition them on top of the ship image.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/28/2026
"""


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen= ai_game.screen
        self.settings=ai_game.settings
        self.color= self.settings.bullet_color

        self.rect= pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midleft = ai_game.ship.rect.midleft
        #the ship is facing towards the left, so the bullets should come out from the middle left

    def update(self):
        self.rect.x -= self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
