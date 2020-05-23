import pygame

class Ship:
    """a class to mange ship"""

    def __init__(self, ai_game):
        """initialising the ship and set its strting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load("/home/shambhu/git_project/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store adecimal value for the ships horizontal position.
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships position based on the movement flag"""
        # update the ships x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0
            self.x += self.settings.ship_speed

        # update rect object from from self.x.
        self.rect.x = self.x 

    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)