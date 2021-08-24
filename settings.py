import pygame
import random


class Settings:
    def __init__(selfse):
        # I'm just realizing, the 'self' argument can be anything
        # It just represents all the attribute of any instances created from this class
        # selfse.screen_width is kind of saying 'the screen_width of an Settings instrance is...'
        selfse.screen_width = 1200
        selfse.screen_length = 800
        selfse.bg_color = (0, 0, 0)

        selfse.bgimage = pygame.image.load("background.png")
        # Bullet Settings
        selfse.bullet_speed = 4.0
        selfse.bullet_width = 3
        selfse.bullet_height = 15
        selfse.bullet_color = (255, 255, 255)
        # Target settings
        selfse.targets_speed = 0.7
        selfse.drop_speed = 1.5
        selfse.direction = 1

        selfse.ship_lives = 3

    def background(self, ai_game):
        # ai_game is an argument, which is the actual game loop of game.py
        # ai_game.screen is saying, take the screen attribute from the AlienInvation class...
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.bgimage_rect = self.bgimage.get_rect()
        self.bgimage_rect.center = self.screen_rect.center
        self.screen.blit(self.bgimage, (60, 200))
