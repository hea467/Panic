import pygame


class Cover:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.cover = pygame.image.load("cover.png")
        self.cover_rect = self.cover.get_rect()
        self.cover_rect.center = self.screen_rect.center

    def draw_cover(self):
        self.screen.blit(self.cover, self.cover_rect)
