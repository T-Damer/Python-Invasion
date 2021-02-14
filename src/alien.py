import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load("../res/images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saving position of an alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ Draws alien in current position"""
        self.screen.blit(self.image, self.rect)
