import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import helpers as hp

def run_game():
    # Initialize
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_hight))
    pygame.display.set_caption("Sideways shooter")

    ship = Ship(settings, screen)
    bullets = Group()

    # Main loop
    while True:
        hp.handle_events(settings, ship, bullets, screen)
        hp.update_bullets(bullets, screen)
        hp.update_screen(screen, settings, ship, bullets)

run_game()