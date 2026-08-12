"""
Alien Invasion
Stuti Pathak
Purpose: Progression of the game statsitcs, such as the player current score, highscore, ships left, and if the game is active, by storing all this information in this class (not displaying).
Starter code: From Python Crash Course book and Python Programming lectures.
8/11/2026
"""
class GameStats:
    def __init__(self, ai_game):
        self.settings= ai_game.settings
        self.high_score=0
        self.reset_stats()
        

    def reset_stats(self):
        self.ships_left= self.settings.ship_lives
        self.score=0
        self.level=1



