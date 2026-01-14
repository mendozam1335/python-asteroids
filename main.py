import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from powerup_field import PowerUp_Field
from shot import Shot
from machinegun import Machinegun

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    PowerUp_Field.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Machinegun.containers = (drawable, powerups, updatable)

    asteroid_field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    powerup_field = PowerUp_Field(ship)

    time = pygame.time.Clock()
    dt = 0
    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if ship.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for powerup in powerups:
            if not powerup.should_collide():
                continue
            if ship.collides_with(powerup):
                log_event("powerup_collected")
                powerup.on_pickup()

        for group in drawable:
            group.draw(screen)

        pygame.display.flip()

        dt = time.tick(60) / 1000 # Delta time in seconds.
        


if __name__ == "__main__":
    main()
