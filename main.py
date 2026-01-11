import pygame
import constants
from logger import log_state

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0
    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        pygame.display.flip()

        dt = time.tick(60) / 1000 # Delta time in seconds.



if __name__ == "__main__":
    main()
