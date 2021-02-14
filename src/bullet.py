import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Creates bullet object in current player position"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()  # Need for correct Sprite working!
        self.screen = screen
        # Creating bullet in 0,0 and moving in to the ship pos
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.bullet_speed_factor = 3

        # Storing bullet position
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self, ai_settings):
        """ Moves bullet to on the screen """
        self.y -= self.bullet_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
