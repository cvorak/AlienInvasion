import pygame

class Ship():
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        self.moving_up = False
        self.moving_down = False

        self.image = pygame.image.load('images/ship_sideways.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.y = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_factor

        self.rect.centery = self.y


