class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_speed_factor = 2

        # Bullet Parameters
        # bullet_speed_factor stored in bullet.py!

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
