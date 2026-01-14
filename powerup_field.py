import pygame
import random
from machinegun import Machinegun
from constants import *

class PowerUp_Field(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self, self.containers)
      self.spawn_chance = 0.1 
      self.spawn_timer = 0.0
      self.powerup_count = 0

    def spawn(self, powerup_type):
      if powerup_type == "machinegun":
          x = random.randint(0, SCREEN_WIDTH)
          y = random.randint(0, SCREEN_HEIGHT)
          machinegun_powerup = Machinegun(x, y)
          print("Spawned machinegun power-up at:", x, y)

    def update(self, dt):
      self.spawn_timer += dt

      if self.spawn_timer >= POWERUP_SPAWN_INTERVAL and self.powerup_count < MAX_POWERUPS:
          print("Checking to spawn power-up...")
          self.spawn_timer = 0.0
          if random.random() < self.spawn_chance:
              self.spawn("machinegun")
              self.powerup_count += 1

    

    

