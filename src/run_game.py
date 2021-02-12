import pygame

from ship import Ship
from alien import Alien
from settings import Settings
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)

    alien = Alien(screen)

    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # Deleting bullets outta screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)



run_game()
