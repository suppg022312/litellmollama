Sure! Here's a simple implementation of the Asteroids game using Python and Pygame library. Please let me know if you need any further assistance.

```python
import pygame

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BORDER = 30
SHIP_WIDTH, SHIP_HEIGHT = 50, 40
ASTEROID_COUNT = 20
ASTEROID_SIZE = 25
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Asteroids')

# Ship class
class Ship:
    def __init__(self):
        self.x = WIDTH // 2 - SHIP_WIDTH // 2
        self.y = HEIGHT // 2 - SHIP_HEIGHT // 2
        self.rect = pygame.Rect(self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT)
        self.moving_left = False

    def move(self):
        if self.moving_left:
            self.x -= 5

        # Check for border collision
        if self.x <= BORDER:
            self.moving_left = False
        elif self.x + self.rect.width >= WIDTH - BORDER:
            self.moving_left = True

# Asteroid class
class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, ASTEROID_SIZE, ASTEROID_SIZE)

    def move(self):
        # Move asteroid down the screen
        if self.y > HEIGHT - ASTEROID_SIZE:
            self.y = -ASTEROID_SIZE

# Game class
class Game:
    def __init__(self):
        self.screen = screen
        self.ship = Ship()
        self.asteroids = [Asteroid(WIDTH // 2, HEIGHT // 2) for _ in range(ASTEROID_COUNT)]

    def run(self):
        # Game loop
        clock = pygame.time.Clock()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with white color
            self.screen.fill(WHITE)

            # Draw ship and asteroids
            for asteroid in self.asteroids:
                self.screen.blit(asteroid.rect, (asteroid.x, asteroid.y))
            self.screen.blit(self.ship.rect, (self.ship.x, self.ship.y))

            # Update screen
            pygame.display.flip()

            # Move everything
            for asteroid in self.asteroids:
                asteroid.move()
            self.ship.move()

    def game_loop(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the screen with white color
            self.screen.fill(WHITE)

            # Draw ship and asteroids
            for asteroid in self.asteroids:
                self.screen.blit(asteroid.rect, (asteroid.x, asteroid.y))
            self.screen.blit(self.ship.rect, (self.ship.x, self.ship.y))

            # Update screen
            pygame.display.flip()

            # Move everything
            for asteroid in self.asteroids:
                asteroid.move()
            self.ship.move()


game = Game()
game.run()
```