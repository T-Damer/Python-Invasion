import pygame

from ship import Ship
from alien import Alien
from settings import Settings
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()  # Very cool trick, you store all setting in one variable!

    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)

    alien = Alien(screen)

    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
