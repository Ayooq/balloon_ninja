import sys
import pygame
from Settings import Settings
from Engine import Engine
from Button import Button
from Instructions import Instructions
from Sword import Sword
from Scoreboard import Scoreboard


def run_game():

    # Get access to our game settings:
    settings = Settings()

    # Initialize game:
    pygame.init()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height), 0, 32
    )
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen, settings)
    play_button = Button(
        screen,
        settings.screen_width / 2 - settings.button_width / 2,
        settings.screen_height / 2 - settings.button_height / 2,
        settings,
        'Play Balloon Ninja')
    game_over_button = Button(
        screen,
        play_button.x_position,
        play_button.y_position - 2 * settings.button_height,
        settings,
        'Game Over'
    )
    instructions = Instructions(screen, settings)

    # Create a list to hold our balloons, and our kittens:
    balloons = []
    kittens = []

    # Create our sword:
    sword = Sword(screen, settings.scoreboard_height)

    # Create our game engine, with access to appropriate game parameters:
    engine = Engine(screen, settings, scoreboard, balloons, kittens, sword)

    # Main event loop:
    while True:
        # Advance our game clock, get the current mouse position,
        # and check for new events:
        time_passed = clock.tick(50)
        mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        engine.check_events(play_button, mouse_x, mouse_y)

        # Redraw the empty screen before redrawing any game objects:
        screen.fill(settings.bg_color)

        if settings.game_active:
            # Update the sword's position,
            # and check for the balloons' & kittens' state:
            engine.update_sword(mouse_x, mouse_y)
            engine.check_balloons(time_passed)
            engine.check_kittens(time_passed)

            # If all balloons have disappeared, either through popping
            # or rising, release a new batch of balloons.
            if len(balloons) == 0:
                # If we're not just starting a game, increase the
                # following values:
                if scoreboard.balloons_popped > 0:
                    settings.balloon_speed *= settings.speed_increase_factor
                    settings.kitten_ratio *= settings.speed_increase_factor
                    settings.points_per_balloon += settings.batch_size
                    scoreboard.batches_finished += 1
                # If player has completed required batches,
                # increase batch_size:
                if scoreboard.batches_finished % settings.batches_needed == 0 \
                        and scoreboard.batches_finished:
                    settings.batch_size += 1
                engine.release_batch()
        else:
            # Game is not active, so...
            # Show play button:
            play_button.blitme()
            # Show instructions for first few games:
            if settings.games_played < 3:
                instructions.blitme()
            # If a game has just ended, show Game Over button:
            if settings.games_played > 0:
                game_over_button.blitme()

        # Display updated scoreboard:
        scoreboard.blitme()

        # Show the redrawn screen:
        pygame.display.flip()

run_game()
