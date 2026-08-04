"""
Alien Invasion
Stuti Pathak
Purpose: The Alien Invasion program is a virtual game, similar to Space Invaders, where the ship controlled by the user on the right side of the screen moves vertically to shoot down aliens coming from the left side of the screen towards with bullets from the space ship. This file is the engine of the game Alien Invasion which runs the game based on the keyboard actions of the player.
Starter code: From Python Crash Course book and Python Programming lectures (Unit 6).
7/27/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings= Settings()
        self.screen= pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion-Track 1")

        self.bg_color= self.settings.bg_color
        self.ship=Ship(self)
        self.bullets= pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()


            for bullet in self.bullets.copy():
                if bullet.rect.right <= 0:
                    self.bullets.remove(bullet)


            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            


    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down= True 
            #the y works opposite, so y+=1 moves the ship 
        elif event.key== pygame.K_UP:
            self.ship.moving_up = True
        elif event.key== pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()



    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down= False
        elif event.key== pygame.K_UP:
            self.ship.moving_up= False


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet= Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        alien= Alien(self)
        alien_height = alien.rect.width
        current_y = alien_height
        while current_y <(self.settings.screen_height -2 * alien_height):
            new_alien = Alien(self)
            new_alien.rect.left=0
            new_alien.rect.y=current_y
            self.aliens.add(new_alien)
            current_y+=2* alien_height
            




if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
