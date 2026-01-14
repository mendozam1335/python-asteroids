from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0.0
        self.current_shoot_cooldown = SHOOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_cooldown -= dt
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        direction = forward * PLAYER_SPEED * dt
        self.position += direction
    
    def shoot(self):
        if self.shoot_cooldown > 0.0:
            return
        self.set_shoot_cooldown(self.current_shoot_cooldown)

        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1) 
        velocity = velocity.rotate(self.rotation)
        velocity *= SHOT_SPEED
        shot.velocity = velocity

    def set_shoot_cooldown(self, cooldown):
        self.shoot_cooldown = self.current_shoot_cooldown
        self.current_shoot_cooldown = cooldown