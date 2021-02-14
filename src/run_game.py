import pygame

from ship import Ship
from settings import Settings
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update(ai_settings)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stars)
        gf.create_fleet(ai_settings, screen, ship, aliens)


run_game()
