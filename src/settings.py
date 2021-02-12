class Settings():
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 640
        self.bg_color = (255, 255, 255)
        # Ship settings
        self.ship_speed_factor = 0.2

        # Bullet Parameters
        # bullet_speed_factor stored in bullet.py!

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
