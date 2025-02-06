Here is a simple implementation of the classic Asteroids game using Python and the Pygame library.

**Asteroids Game in Python**
==========================

### Requirements

* Python 3.x
* Pygame library (`pip install pygame`)

### Code

```python
import pygame
import math
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = 0
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 20

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, (
            (self.x + math.cos(math.radians(self.angle)) * self.radius, self.y - math.sin(math.radians(self.angle)) * self.radius),
            (self.x + math.cos(math.radians(self.angle - 120)) * self.radius, self.y - math.sin(math.radians(self.angle - 120)) * self.radius),
            (self.x + math.cos(math.radians(self.angle + 120)) * self.radius, self.y - math.sin(math.radians(self.angle + 120)) * self.radius)
        ))

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, 360)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.radius = random.randint(10, 30)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = -5
        self.radius = 2

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ship = Ship()
    asteroids = [Asteroid() for _ in range(5)]
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship.x, ship.y))
                elif event.key == pygame.K_w:
                    ship.speed_y -= 2
                elif event.key == pygame.K_s:
                    ship.speed_y += 2
                elif event.key == pygame.K_a:
                    ship.angle += 5
                elif event.key == pygame.K_d:
                    ship.angle -= 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            ship.speed_y -= 1
        if keys[pygame.K_s]:
            ship.speed_y += 1
        if keys[pygame.K_a]:
            ship.angle += 2
        if keys[pygame.K_d]:
            ship.angle -= 2

        ship.update()
        for asteroid in asteroids:
            asteroid.update()

        screen.fill(BLACK)
        ship.draw(screen)

        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)
            for asteroid in asteroids:
                distance = math.sqrt((bullet.x - asteroid.x) ** 2 + (bullet.y - asteroid.y) ** 2)
                if distance < bullet.radius + asteroid.radius:
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)

        for asteroid in asteroids[:]:
            screen.blit(pygame.Surface((WIDTH, HEIGHT)), (0, 0))
            asteroid.draw(screen)
            distance = math.sqrt((ship.x - asteroid.x) ** 2 + (ship.y - asteroid.y) ** 2)
            if distance < ship.radius + asteroid.radius:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```

### How to Play

* Use the W and S keys to move up and down.
* Use the A and D keys to turn left and right.
* Press the space bar to shoot bullets.
* Destroy all asteroids to win!

Note: This is a basic implementation of Asteroids, you can add more features like scorekeeping, lives, and smoother graphics.