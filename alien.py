"""
Alien Invasion
Stuti Pathak
Purpose: This is the class designed to control the aliens.
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
        self.rect = self.image.get_rect()


        self.rect.x= self.rect.width
        self.rect.y= self.rect.height

        
