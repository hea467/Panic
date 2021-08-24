import pygame


class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        # The game screen is named self.screen
        # get_rect() gets the coordinates
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # The image of the ship is named self.image
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        # Treat the image like a rectangle and stores the coordinates

        # The bottom of the ship image is the same as the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 4
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 4

    # Draw the ship at its coordinate
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
