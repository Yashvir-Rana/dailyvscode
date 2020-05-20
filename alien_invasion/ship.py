import pygame

class Ship:
    """a class to mange ship"""

    def __init__(self, ai_game):
        """initialising the ship and set its strting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load("/home/shambhu/git_project/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)