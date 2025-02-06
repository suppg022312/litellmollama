Here is a simple implementation of the classic Asteroids game in Python using the Pygame library.

```python
import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
SHIP_SPEED = 5
ENEMY_SPEED = 3
LASER_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the player ship class
class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = math.pi / 4
        self.speed = SHIP_SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y += math.sin(self.angle) * self.speed
        if keys[pygame.K_DOWN]:
            self.y -= math.sin(self.angle) * self.speed
        if keys[pygame.K_LEFT]:
            self.x -= math.cos(self.angle) * self.speed
        if keys[pygame.K_RIGHT]:
            self.x += math.cos(self.angle) * self.speed

    def draw(self):
        pygame.draw.polygon(screen, WHITE, (
            (self.x + math.sin(self.angle) * 20, self.y - math.cos(self.angle) * 20),
            (self.x + math.sin(self.angle) * 40, self.y - math.cos(self.angle) * 40),
            (self.x + math.sin(self.angle) * 20, self.y - math.cos(self.angle) * 60)
        ))

# Define the enemy class
class Enemy:
    def __init__(self):
        self.x = pygame.randint(0, WIDTH)
        self.y = pygame.randint(0, HEIGHT)

    def move(self):
        self.x += ENEMY_SPEED

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 20)

# Define the laser class
class Laser:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += math.cos(self.angle) * LASER_SPEED

    def draw(self):
        pygame.draw.line(screen, WHITE, (int(self.x), int(self.y)), (int(self.x + math.cos(self.angle) * 50), int(self.y - math.sin(self.angle) * 50)))

# Create the player ship
ship = Ship()

# Create a list of enemies
enemies = [Enemy() for _ in range(10)]

# Create a list of lasers
lasers = []

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ship
    ship.move()

    # Move the enemies
    for enemy in enemies:
        enemy.move()
        if enemy.x > WIDTH:
            enemy.x = 0

    # Create new lasers when space is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        laser_angle = math.atan2(ship.y - pygame.mouse.get_pos()[1], ship.x - pygame.mouse.get_pos()[0])
        lasers.append(Laser(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], laser_angle))

    # Move and draw the enemies
    for enemy in enemies:
        if (ship.x - enemy.x) ** 2 + (ship.y - enemy.y) ** 2 < 100:
            print("Game Over")
            pygame.quit()
            sys.exit()
        else:
            screen.fill(BLACK)
            ship.draw()
            for laser in lasers[:]:
                laser.move()
                if (laser.x > enemy.x and laser.x < enemy.x + 40 and
                    laser.y - 20 < enemy.y < laser.y + 20):
                    lasers.remove(laser)
                    enemies.remove(enemy)
                    break

            for enemy in enemies:
                enemy.draw()

            for laser in lasers:
                laser.draw()
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

```

This code creates a game window with a ship that you can control using the arrow keys. You can shoot lasers by pressing the space bar, and the game ends when an enemy collides with the ship.

Please note that this is a very basic implementation of Asteroids, and there's much room for improvement (such as adding more features like scorekeeping, smoother animation, or even AI-controlled enemies).