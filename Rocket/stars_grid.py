import sys
import pygame
from pygame.sprite import Group

from star import Star

def show_stars_grid():
    # Initialize grid 1000x1000px, stars are images 100x100px.
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Stars...")
    star = Star(screen)
    stars = Group()
    horisontal_number = int(screen.get_rect().width / star.rect.width)
    star_side = star.rect.width
    vertical_number = int(screen.get_rect().height / star.rect.height)
    for star_vertical_number in range(vertical_number):
        for star_horisontal_number in range(horisontal_number):
            x_position = star_horisontal_number * star_side
            y_position = star_vertical_number * star_side
            star = Star(screen)
            star.rect.x = x_position
            star.rect.y = y_position
            stars.add(star)

    stars.draw(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



show_stars_grid()