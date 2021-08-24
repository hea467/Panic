import pygame.font


class Scores:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_score()
        self.prep_lives()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0, 0, 0))

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = (self.screen_rect.right) - 10
        self.score_rect.top = 10

    def print_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def prep_lives(self):
        lives_str = "lives left: " + str(self.stats.ship_left)
        self.lives_image = self.font.render(lives_str, True, self.text_color, (0, 0, 0))
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 20
        self.lives_rect.top = 10

    def print_lives(self):
        self.screen.blit(self.lives_image, self.lives_rect)
