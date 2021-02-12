import pygame


class Alien:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("../res/images/alien.bmp").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship begins from the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        """ Draws ship in current position"""
        self.screen.blit(self.image, self.rect)
