import pygame

from time import sleep


class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """ Initializes ingame statistics """
        self.ships_left = self.ai_settings.ship_limit

    def game_over(self):
        if not self.game_active:
            pygame.image.load("../res/images/game_over_screen.jpg")
            sleep(1)
            self.game_active = True
