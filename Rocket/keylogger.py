import sys
import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Keylogger")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill((30, 200, 150))
        pygame.display.flip()

run_game()


