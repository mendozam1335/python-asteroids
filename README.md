# Asteroids

Asteroids mini game created using python, pygame, and uv package manager

## Usage

Use standard AWSD keys to move forward backward and rotate left and right.

use 'SPACE' bar to shoot

Collect power ups to increase fire rate temporarily or increase ship movement

## Quit Game

To quit the game simply close the window

## Code Specifics

```python
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <+ (self.radius + other.radius)
```

Every object inherits from circle shape for easier collision detection, rotation, and drawing.
Update is called on every object in main using pygames groups
Draw is similarly called on every drawable object using pygames groups
This allows for multiple objects to be drawn without needing to manually call their draw function every frame

```python
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

while true:
  updatable.update()

  for obj in drawable:
    obj.draw()
```

## Asteroid Spawning

Asteroid field is responsible for spawning asteroid objects from outside the screen.
It is also responsible for handling when large asteroids get shot and need to break down to smaller asteroids.
The field chooses one of the 4 edges of the screen, selects a random direction between -30 and 30 degrees, and sets
the spawn of the asteroid outside the edge.

```python
class Asteroid_field(CircleShape):
# ......

def update(self, dt):
    self.spawn_timer += dt
    if self.spawn_timer > ASTEROID_SPAWNE_RATE_SECONDS:
      self.spawn_timer = 0.0

      edge = random.choice(self.edges)
      speed = random.randint(40,100)
      velocity = edge[0] * speed
      velocity = velocity.rotate(random.randint(-30,30))
      position = edge[1](random.uniform(0,1))
      kind = random.randint(1, ASTEROID_KINDS)
      self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
```

Similarly, the powerup fields spawns the powerups.
Only two power ups active at one time and have a set timer and chance to spawn,

For testing purposes, chance is set to 100 percent so as long as timer is done and there are no more than the max (2), then a powerup will always spawn somewhere.

Powerups inherit from class PowerUp()
This allows me to simply create a new powerup with different affects and add the name to the list in Powerup_fields

```python
class PowerUp_Field(pygame.sprite.sprite):
# ...
powerUps = [Machinegun, Speedup]

 def update(self, dt):
      self.spawn_timer += dt

      if self.spawn_timer >= POWERUP_SPAWN_INTERVAL and self.powerup_count < MAX_POWERUPS:
          self.spawn_timer = 0.0
          if random.random() < self.spawn_chance:
              pu = random.choice(self.powerUps)
              self.spawn(pu)
              self.powerup_count += 1

```

### Contributions

boot.dev
icons provide by

```html
<a href="https://www.flaticon.com/free-icons/asteroid" title="asteroid icons"
  >Asteroid icons created by Good Ware - Flaticon</a
>
<a href="https://www.flaticon.com/free-icons/asteroid" title="Asteroid icons"
  >Asteroid icons created by Freepik - Flaticon</a
>
```
