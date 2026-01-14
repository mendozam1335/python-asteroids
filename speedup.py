import pygame
from constants import *
from powerup import PowerUp

class Speedup(PowerUp):
    def __init__(self, x, y, player):
        super().__init__(x, y, POWERUP_RADIUS, "speedup", player)
        self.speed_multiplier = SPEEDUP_MULTIPLIER
        self.duration = SPEEDUP_DURATION

    def draw(self, screen):
      if not self.should_draw():
        return
      pygame.draw.polygon(screen, "green", self.hexagon(), LINE_WIDTH)
    
    def apply_effect(self):
        self.player.current_speed *= self.speed_multiplier

    def remove_effect(self):
        self.player.current_speed = PLAYER_SPEED
        self.kill()

    def update(self, dt):
        if not self.collected:
            return
            
        self.duration -= dt
        if self.duration <= 0.0:
            self.remove_effect()