import pygame
import random
from machinegun import Machinegun
from speedup import Speedup
from constants import *
from logger import log_event
class PowerUp_Field(pygame.sprite.Sprite):
    powerUps = [Machinegun, Speedup]

    def __init__(self, player=None):
      pygame.sprite.Sprite.__init__(self, self.containers)
      self.spawn_chance = POWERUP_CHANCE
      self.spawn_timer = 0.0
      self.powerup_count = 0
      self.player = player

    def spawn(self, pu):
          x = random.randint(10, SCREEN_WIDTH - 10)
          y = random.randint(10, SCREEN_HEIGHT - 10)
          powerup = pu(x, y, self.player)
          print(f"Spawning powerup: {pu.__name__} at {x, y}" )

    def update(self, dt):
      self.spawn_timer += dt

      if self.spawn_timer >= POWERUP_SPAWN_INTERVAL and self.powerup_count < MAX_POWERUPS:
          
          self.spawn_timer = 0.0
          if random.random() < self.spawn_chance:
              pu = random.choice(self.powerUps)
              self.spawn(pu)
              self.powerup_count += 1

    

    

