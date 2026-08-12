"""
Alien Invasion
Stuti Pathak
Purpose: The Button class displays the Play button of the game on the screen center, allowing the player to decide when to start the game by clicking on the button. This class controlls the Play button functions to start the game and showcase the button as well.
Starter code: From Python Crash Course book and Python Programming lectures.
8/11/2026
"""
import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect= self.screen.get_rect()

        self.width, self.height= 200, 50
        self.button_color= (0, 135, 0)
        self.text_color= (255, 255, 255)
        self.font= pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg= msg
        self._prep_msg()

       
    
    def _prep_msg(self):
      self.msg_image= self.font.render(self.msg, True, self.text_color, self.button_color)
      self.msg_image_rect= self.msg_image.get_rect()
      self.msg_image_rect.center= self.rect.center

    def draw_button(self):
       self.screen.fill(self.button_color, self.rect)
       self.screen.blit(self.msg_image, self.msg_image_rect)



