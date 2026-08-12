"""
Alien Invasion
Stuti Pathak
Purpose: The Alien Invasion program is a virtual game, similar to Space Invaders, where the ship controlled by the user on the right side of the screen moves vertically to shoot down aliens coming from the left side of the screen towards with bullets from the space ship. This file is the engine of the game Alien Invasion which runs the game based on the keyboard actions of the player.
Starter code: From Python Crash Course book and Python Programming lectures.
7/27/2026
"""

import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()


        self.game_active= False

        self.settings= Settings()
        self.screen= pygame.display.set_mode(self.settings.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion-Track 1")

        self.bg_color= self.settings.bg_color
        self.ship=Ship(self)
        self.bullets= pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()

        self.stats= GameStats(self)

        self.play_button= Button(self, "Play")
        

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions= pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) 

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type== pygame.MOUSEBUTTONDOWN:
                mouse_pos= pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked= self.play_button.rect.collidepoint(mouse_pos) 
        if  button_clicked and not self.game_active:
            self._reset_game()


    def _reset_game(self):
        self.stats.reset_stats()
        self.game_active=True
        
        self.bullets.empty()
        self.aliens.empty()
        
        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)
        self.settings.intialize_dynamic_settings()


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

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        alien= Alien(self)
        alien_width= alien.rect.width
        alien_height = alien.rect.height
        current_y, current_x = alien_height, alien_width

        while current_x < (self.settings.screen_width - 3 * alien_width):
            current_y= alien_height
            while current_y <(self.settings.screen_height -2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y+=2* alien_height

            current_x+=2* alien_height
            current_y= alien_height
            


    def _create_alien(self,x_position, y_position):
        new_alien = Alien(self)
        new_alien.rect.x= x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # has the alien ship collided with the player ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        

    def _ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()


            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active= False
            pygame.mouse.set_visible(True)
       



    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break

    def _check_fleet_direction(self):
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_width:
                self._ship_hit()
                break

    



if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
