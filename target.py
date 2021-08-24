import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game

        self.image = pygame.image.load("target.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.settings = ai_game.settings

    # To check if the target is at the edge of screen

    # Change direction
    def update(self):
        self.x += self.settings.targets_speed * self.settings.direction
        self.rect.x = self.x
        self.y += self.settings.drop_speed
        self.rect.y = self.y
