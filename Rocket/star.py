import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        # Load the image and set the rect.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        # Position every new star in the top left corner.
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        """Draw the star at its current location"""
        self.screen.blit(self.image, self.rect)
