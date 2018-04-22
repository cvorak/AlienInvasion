import sys
import pygame
from bullet import Bullet

def handle_events(settings, ship, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, event, ship, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(settings, event, ship, screen, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < settings.max_bullets:
            new_bullet = Bullet(settings, ship, screen)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(screen, settings, ship, bullets):
    screen.fill(settings.bg_color)
    ship.update()
    bullets.update()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()

def update_bullets(bullets, screen):
    for bullet in bullets.copy():
        if bullet.rect.right > screen.get_rect().right:
            bullets.remove(bullet)
