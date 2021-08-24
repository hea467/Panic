class Stats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        self.game_running = False
        self.score = 0

    def reset_stats(self):
        self.ship_left = self.settings.ship_lives
        self.settings.drop_speed = 1.5  # Increases speed of the target descent
        self.settings.targets_speed = 0.7
        self.settings.ship_lives=3
