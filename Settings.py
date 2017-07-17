class Settings():
    """Game settings class.

    Sets up in-game parameters and the screen attributes.
    """
    def __init__(self):

        # Screen parameters:
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = 200, 200, 200
        self.scoreboard_height = 50

        self.button_width, self.button_height = 250, 50
        self.button_bg = (0, 163, 0)
        self.button_text_color = (235, 235, 235)
        self.button_font, self.button_font_size = 'Arial', 24

        # Game status:
        self.game_active = False

        # Game over conditions:
        self.min_popped_ratio = 0.9
        self.games_played = 0

        self.initialize_game_parameters()

    def initialize_game_parameters(self):
        """Gameplay parameters."""
        self.balloon_speed = 0.1
        # How quickly the speed of balloons rises
        self.speed_increase_factor = 1.03
        self.points_per_balloon = 10

        # Number of balloons to release in a spawning:
        self.batch_size = 1
        # Number of batches that must be completed to increment batch_size:
        self.batches_needed = 3
        # Ratio of kittens released per balloon released:
        self.kitten_ratio = 0.10
        # Relative value of kittens, in terms of balloons:
        self.kitten_score_factor = 3
