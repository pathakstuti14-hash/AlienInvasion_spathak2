#keeps track of how many ships left, adding up points, and score of the game.
"""
Alien Invasion
Stuti Pathak
This class is to store all the settings of the game, including screen width, height, background color, and speed for the various objects, and the size of the objects (bullets, ship, aliens).
Starter code: From Python Crash Course book and Python Programming lectures.
7/27/2026
"""
class GameStats:
    def __init__(self, ai_game):
        self.settings= ai_game.settings
        self.reset_stats()
        self.game_active= False

    def reset_stats(self):
        self.ships_left= self.settings.ship_lives
        