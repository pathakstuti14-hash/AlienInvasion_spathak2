"""
Alien Invasion
Stuti Pathak
The Alien Invasion program is a virtual game, similar to Space Invaders, where the ship controlled by the user on the right side of the screen moves vertically to shoot down aliens coming from the left side of the screen towards with bullets from the space ship. This file is the engine of the game Alien Invasio.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""

import sys
import pygame

if __name__ == '__main__':
    pass

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen= pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("Alien Invasion")

    
