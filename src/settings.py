import math


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_speed_factor = 2
        self.ship_limit = 2

        # Bullet Parameters
        # bullet_speed_factor stored in bullet.py!

        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_speed_factor = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Aliens settings

        self.alien_speed_factor = 0.2
        self.fleet_direction = 1
        self.fleet_drop_speed = 50

        # Hard level settings. Game Tempo
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Settings, that changes in game and resets after game end"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        self.alien_points = 50

        # fleet_direction = 1 - moves right, -1 - moves left

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = math.ceil(self.alien_speed_factor * 1.5)
