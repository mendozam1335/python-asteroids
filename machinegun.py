from circleshape import CircleShape
import pygame
from constants import *
from powerup import PowerUp

class Machinegun(PowerUp):
    def __init__(self, x, y, player):
        super().__init__(x, y, POWERUP_RADIUS, "machinegun", player)
        self.rate_of_fire = MACHINEGUN_RATE_OF_FIRE
        self.duration = MACHINEGUN_DURATION

    def draw(self, screen):
      if not self.should_draw():
        return
      pygame.draw.polygon(screen, "blue", self.hexagon(), LINE_WIDTH)
    
    def apply_effect(self):
        self.player.set_shoot_cooldown(self.rate_of_fire)

    def remove_effect(self):
        self.player.set_shoot_cooldown(SHOOT_COOLDOWN)
        self.kill()

    def update(self, dt):
        if not self.collected:
            return
            
        self.duration -= dt
        if self.duration <= 0.0:
            self.remove_effect()


