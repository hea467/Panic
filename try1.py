import sys
import pygame
import random
from time import sleep

from pygame import sprite

from settings import Settings
from ship import Ship
from pygame.constants import K_RIGHT
from bullets import Bullets
from target import Target
from stats import Stats
from cover import Cover
from scoreboard import Scores


class AlienInvasion:
    # Overall class

    def __init__(self):  # Making ome basics available to later methods
        pygame.init()  # Initializes background works for pygame to function
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_length = self.screen.get_rect().height
        pygame.display.set_caption("Panic!")
        self.background = Settings()
        self.stats = Stats(self)
        self.scores = Scores(self)
        self.ship = Ship(self)  # sets up the class to have linked attributes
        # ai_game=self so the dimensions gets passed mainly for screen centering
        self.bullets = pygame.sprite.Group()
        # returns a list of all sprites (bullets) in the group
        # interating can allow all sprites to have the same attribute
        # the sprites are created by creating a child class from Sprite
        self.targets = pygame.sprite.Group()
        self.create_fleet()
        self.cover_art = Cover(self)

    def run_game(self):  # The game runs because the loop in this method refreshes
        while True:  # Infinite loop untill stopped
            self.check_events()
            if self.stats.game_running == True:
                self.ship.update()  # Updates the position of the ship
                # update function is written in the class ship
                self.update_bullets()
                self.update_targets()
            self.update_screen()

    def check_events(self):  # Took out underscore in front bc encapsulation is useless
        for event in pygame.event.get():
            # Returns a list of all events since the last repetition
            if event.type == pygame.QUIT:
                sys.exit()  # Tells the system to exit the file directly.
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mposition = pygame.mouse.get_pos()
                # Returns a tuple with x,y coordinates
                if (
                    self.cover_art.cover_rect.collidepoint(mposition)
                    and not self.stats.game_running
                ):
                    # When the cover is clicked the game is not yet active!
                    # Checks of mposition collides with the rect of the cover
                    self.targets.empty()
                    self.stats.reset_stats()  # Also resets the target speed
                    self.bullets.empty()
                    self.stats.game_running = True
                    self.create_fleet()
                    self.ship.center_ship()
                    self.stats.score = 0
                    self.scores.prep_score()
                    self.scores.print_score()
                    self.scores.prep_lives()
                    self.scores.print_score()

    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        new_bullet = Bullets(self)
        if len(self.bullets) < 4:
            self.bullets.add(
                new_bullet
            )  # Like append but specifically for pygame group
        # creates an instance new bullet from class Bullets

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # The format here is kinda of saying...
        #'The screen of the Alien Invation class instance (self) is...'
        self.settings.background(self)
        self.ship.blitme()
        if self.stats.game_running:
            self.targets.draw(self.screen)
            for bullet in self.bullets.sprites():
                # self.bullet=spire group, then sprites() function
                bullet.draw_bullet()  # from bullets class draw it on screen

        self.scores.print_score()
        self.scores.print_lives()
        if not self.stats.game_running:
            self.cover_art.draw_cover()

        pygame.display.flip()  # Make the most recently drawn screen available

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
        # Check for collisions between two sprites groups
        collisions = pygame.sprite.groupcollide(self.bullets, self.targets, True, True)
        if collisions:
            self.stats.score += 50
            self.scores.prep_score()

    def create_fleet(self):
        for i in range(2):
            target = Target(self)
            target.y = -100
            target.rect.y = target.y
            target.x = random.randint(100, 1100)
            target.rect.x = target.x
            self.targets.add(target)

    def create_new_fleet(self):
        target = Target(self)
        target.y = -100
        target.rect.y = target.y
        target.x = random.randint(400, 1000)
        target.rect.x = target.x
        self.settings.direction = random.random() + random.randint(-2, 2)
        self.targets.add(target)

    def update_targets(self):
        self.targets.update()
        self.check_target_y()
        for target in self.targets:
            screen_rect = self.screen.get_rect()
            # One method you can check edges
            if target.rect.right > screen_rect.right:
                self.settings.direction = -1
            # Anothe method...
            if target.rect.x < 10:
                self.settings.direction = 1
            # if target.rect.bottom >= screen_rect.bottom:
            # self.ship_hit() => Alternate method for bottom check and restart
        if pygame.sprite.spritecollideany(self.ship, self.targets):
            self.ship_hit()

        if len(self.targets) < 2:
            self.create_new_fleet()
            self.settings.drop_speed += 0.008  # Increases speed of the target descent
            self.settings.targets_speed += 0.01  # Upon the next new fleet called, slows the speed by one instance lol

    def ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            # Clear the targets and bullets on screen
            self.targets.empty()
            self.bullets.empty()
            # Create new targets
            self.create_new_fleet()
            # Move the ship back to the center
            self.ship.center_ship()
            self.scores.prep_lives()
            sleep(0.5)
        else:
            self.stats.game_running = False

    def check_target_y(self):
        for target in self.targets.sprites():
            screen_rect = self.screen.get_rect()
            if target.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break  # You need to reset the game if just one instance hits


if __name__ == "__main__":
    # makes sure lines below can only be run from this file
    ai = AlienInvasion()  # Creates an instance of the game
    ai.run_game()  # Calls the run_game method
