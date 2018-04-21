class Settings():
    """A Class to store all settings for Rocket game"""

    def __init__(self):
        """Init the game's settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (250, 250, 250)

        # Ship settings
        self.rocket_speed_coefitient = 1.5
