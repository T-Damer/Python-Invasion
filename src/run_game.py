import pygame

from ship import Ship
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    stats = GameStats(ai_settings)

    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_fleet(ai_settings, screen, ship, stats, sb, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)


run_game()
