import pygame
from constants import *
from circleshape import CircleShape

class PowerUp(CircleShape):
    def __init__(self, x, y, radius, powerup_type, player):
        super().__init__(x, y, POWERUP_RADIUS)
        self.type = powerup_type

        self.collected = False
        self.dead = False
        self.player = player
    
    def hexagon(self):
      top = pygame.Vector2(0,1) * self.radius
      a = self.position + top.rotate(30)
      b = self.position + top.rotate(90)
      c = self.position + top.rotate(150)
      d = self.position + top.rotate(210)
      e = self.position + top.rotate(270)
      f = self.position + top.rotate(330)
      return [a, b, c, d, e, f]

    def on_pickup(self):
        self.collected = True
        self.apply_effect()

    def draw(self, screen):
        pass
    
    def update(self, dt):
        pass
    
    def apply_effect(self):
        pass
    
    def remove_effect(self):
        pass
    
    def should_draw(self) -> bool:
      return not self.collected
    
    def should_collide(self) -> bool:
      return not self.collected

