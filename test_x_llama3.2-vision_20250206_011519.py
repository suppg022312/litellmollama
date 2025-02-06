Here's a simple implementation of the classic Asteroids game using Python and the Pygame library. This code includes basic features like movement, shooting, scoring, and collision detection.

**asteroids.py**
```python
import pygame
import math
import random

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Ship(pygame.Rect):
    def __init__(self):
        super().__init__(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50, 30, 30)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed_y -= 1
        if keys[pygame.K_DOWN]:
            self.speed_y += 1
        if keys[pygame.K_LEFT]:
            self.speed_x -= 1
        if keys[pygame.K_RIGHT]:
            self.speed_x += 1

        self.x += self.speed_x
        self.y += self.speed_y

        # Boundary checking
        if self.left < 0:
            self.left = 0
        elif self.right > WINDOW_WIDTH:
            self.right = WINDOW_WIDTH
        if self.top < 0:
            self.top = 0
        elif self.bottom > WINDOW_HEIGHT:
            self.bottom = WINDOW_HEIGHT

    def shoot(self):
        return Bullet(self.centerx, self.centery)

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 10)
        self.speed_y = -15
        self.speed_x = random.randint(-2, 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT - 50), 20, 20)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.ship = Ship()
        self.bullets = []
        self.asteroids = [Asteroid() for _ in range(5)]
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not any(b.colliderect(self.ship) for b in self.bullets):
                    self.bullets.append(self.ship.shoot())

    def update(self):
        self.ship.move()
        for asteroid in self.asteroids:
            asteroid.move()
            if self.ship.colliderect(asteroid):
                print("Game Over")
                pygame.quit()
                quit()
            for bullet in self.bullets[:]:
                if bullet.colliderect(asteroid):
                    self.score += 1
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.asteroids.append(Asteroid())
        for bullet in self.bullets:
            bullet.move()
            if bullet.left < 0 or bullet.right > WINDOW_WIDTH or bullet.top < 0 or bullet.bottom > WINDOW_HEIGHT:
                self.bullets.remove(bullet)

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.ellipse(self.screen, WHITE, self.ship)
        for asteroid in self.asteroids:
            pygame.draw.ellipse(self.screen, WHITE, asteroid)
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, WHITE, bullet)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(text, (10, 10))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
```
To run this code, save it to a file named `asteroids.py` and install the Pygame library if you haven't already (`pip install pygame`). Then, simply run the script with Python (`python asteroids.py`).

This implementation includes:

* Basic movement controls for the ship
* Shooting bullets using the space bar
* Scoring system
* Collision detection between the ship, bullets, and asteroids
* Game over screen when the ship collides with an asteroid

Note that this is a simplified version of the classic Asteroids game. You can add more features like power-ups, multiple types of asteroids, or a high score table to make it more interesting!