"""
Alien Invasion
Stuti Pathak
This class is designed for the ship object the player uses throughout the game, so the ship class will keep track of the it's own rectangular area during the game.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""


import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen= ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.image= pygame.image.load('images/ship.bmp')
        self.rect= self.image.get_rect()
        self.rect.midright= self.screen_rect.midright
        self.moving_down = False
    def update(self):
        if self.moving_down:
            self.rect.y+=1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


