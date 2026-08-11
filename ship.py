"""
Alien Invasion
Stuti Pathak
Purpose: This class is designed for the ship object the player uses throughout the game, the ship is controlled by the player, and will move up down the screen the right side of the screen.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""


import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen= ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings= ai_game.settings

        self.image= pygame.image.load('images/ship.bmp')
        self.image= pygame.transform.rotate(self.image, 90)
        #this will rotate the ship 270 degrees by calling on the old image, and storing the new rotation for self.image
        self.rect= self.image.get_rect()
        self.center_ship()
        self.moving_down = False
        self.moving_up = False
    


    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.rect.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0: 
            self.rect.y -= self.settings.ship_speed

            
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
      self.rect.midright= self.screen_rect.midright


