import pygame
import random
from machinegun import Machinegun
from constants import *

class PowerUp_Field(pygame.sprite.Sprite):
    powerUps = [Machinegun]
    def __init__(self, player=None):
      pygame.sprite.Sprite.__init__(self, self.containers)
      self.spawn_chance = POWERUP_CHANCE
      self.spawn_timer = 0.0
      self.powerup_count = 0
      self.player = player

    def spawn(self, pu):
          # x = random.randint(0, SCREEN_WIDTH)
          # y = random.randint(0, SCREEN_HEIGHT)
          powerup = pu(SCREEN_WIDTH /2, SCREEN_HEIGHT /2, self.player)
          print("Spawned machinegun power-up")

    def update(self, dt):
      self.spawn_timer += dt

      if self.spawn_timer >= POWERUP_SPAWN_INTERVAL and self.powerup_count < MAX_POWERUPS:
          print("Checking to spawn power-up...")
          self.spawn_timer = 0.0
          if random.random() < self.spawn_chance:
              pu = random.choice(self.powerUps)
              self.spawn(pu)
              self.powerup_count += 1

    

    

