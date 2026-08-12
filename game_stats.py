#keeps track of how many ships left, adding up points, and score of the game.
"""
Alien Invasion
Stuti Pathak
Purpose: Progression of game kept trac
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
        


