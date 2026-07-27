import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen= ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.image= pygame.image.load('image/ship.bmp')
        self.rect= self.image.get_rect()
        self.rect.midrightside= self.screen_rect.midrightside

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

