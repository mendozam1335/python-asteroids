from circleshape import CircleShape
import pygame
from constants import *

class Machinegun(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)
        self.rate_of_fire = MACHINEGUN_RATE_OF_FIRE
        self.duration = MACHINEGUN_DURATION
        
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, LINE_WIDTH)