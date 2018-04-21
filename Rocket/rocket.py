import pygame

class Rocket():

    def __init__(self, settings,  screen):
        """Initialize a rocket and set its starting position."""
        self.screen = screen
        self.settings = settings

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start with the rocket at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
       
    def update(self):
        """Update rocket's position based on a movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.rocket_speed_coefitient
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.settings.rocket_speed_coefitient
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.rocket_speed_coefitient
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.rocket_speed_coefitient

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)

