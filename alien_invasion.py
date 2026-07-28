"""
Alien Invasion
Stuti Pathak
The Alien Invasion program is a virtual game, similar to Space Invaders, where the ship controlled by the user on the right side of the screen moves vertically to shoot down aliens coming from the left side of the screen towards with bullets from the space ship. This file is the engine of the game Alien Invasion.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings= Settings()
        self.screen= pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

        self.bg_color= self.settings.bg_color
        self.ship=Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_DOWN:
                      self.ship.rect.y+=1
                   #the y works opposite, so y+=1 moves the ship down
                   


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
