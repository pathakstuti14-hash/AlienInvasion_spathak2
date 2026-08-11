#keeps track of how many ships left, adding up points, and score of the game.

class GameStats:
    def __init__(self, ai_game):
        self.settings= ai_game.settings
        self.reset_stats()
        self.game_active= False

    def reset_stats(self):
        self.ships_left= self.settings.ship_lives
        