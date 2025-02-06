Here's an example of a simple Asteroids game created using Python with the Pygame library.

```python
import pygame
import sys
import math
import random

# Pygame Initialization
pygame.init()

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Ship class
class Ship:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.angle = 0
        self.speed_x = 5
        self.speed_y = 5

    def draw(self, screen):
        ship_head = [self.x + math.cos(math.radians(self.angle)) * 20,
                     self.y - math.sin(math.radians(self.angle)) * 20]
        ship_tail = [self.x + math.cos(math.radians(self.angle + 180)) * 20,
                     self.y - math.sin(math.radians(self.angle + 180)) * 20]

        pygame.draw.line(screen, WHITE, ship_head, ship_tail, 5)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5

# Asteroid class
class Asteroid:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 20)

    def update(self):
        self.x += math.cos(math.radians(self.angle)) * 1
        self.y -= math.sin(math.radians(self.angle)) * 1

# Bullet class
class Bullet:
    def __init__(self, ship_x, ship_y, ship_angle):
        self.x = ship_x
        self.y = ship_y
        self.speed_x = math.cos(math.radians(ship_angle))
        self.speed_y = -math.sin(math.radians(ship_angle))

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), 5)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

# Player class
class Player:
    def __init__(self):
        self.ship = Ship()
        self.asteroids = [Asteroid() for _ in range(10)]
        self.bullets = []

    def draw(self, screen):
        self.ship.draw(screen)
        for asteroid in self.asteroids:
            asteroid.draw(screen)

    def update(self):
        self.ship.update()

        # Move bullets
        for bullet in self.bullets[:]:
            bullet.update()
            if (bullet.x < 0 or bullet.x > SCREEN_WIDTH or
                bullet.y < 0 or bullet.y > SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        # Check collision with asteroids
        for asteroid in self.asteroids:
            distance = math.sqrt((self.ship.x - asteroid.x) ** 2 +
                                 (self.ship.y - asteroid.y) ** 2)
            if distance < 50 and not (abs(self.ship.angle - asteroid.angle) > 30):
                self.asteroids.remove(asteroid)

        # Check collision with edge
        if (self.ship.x < 0 or self.ship.x > SCREEN_WIDTH or
            self.ship.y < 0 or self.ship.y > SCREEN_HEIGHT):
            print("Game over")
            pygame.quit()
            sys.exit()

# Initialize game loop
def main():
    clock = pygame.time.Clock()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(player.ship.x, player.ship.y, player.ship.angle))

        # Fill background with black
        screen.fill((0, 0, 0))

        # Update game state
        player.update()

        # Draw game elements
        player.draw(screen)

        # Limit frame rate to 60 FPS
        clock.tick(60)

if __name__ == "__main__":
    main()
```

This code creates a simple Asteroids game where you control a ship with your keyboard and shoot bullets. The goal is to avoid asteroids while shooting them down.

The game loop continually updates the game state, draws the game elements, and checks for collisions between the ship and asteroids. If the ship collides with an asteroid or hits the edge of the screen, the game ends.

To play the game, run the script, and use the left and right arrow keys to control the ship's angle and space bar to shoot bullets.