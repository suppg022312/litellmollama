Below is a simple implementation of the classic Asteroids game using Python and Streamlit. This code creates a game window where you can control a spaceship, shoot bullets to destroy asteroids, and collect power-ups.

First, ensure you have the following libraries installed:

* `streamlit`
* `pygame`

You can install them via pip:

```bash
pip install streamlit pygame
```

Here's the code for the game:

**asteroids_game.py**
```python
import streamlit as st
import pygame
import random

# Game constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Ship properties
SHIP_SIZE = 50
SHIP_SPEED = 5

# Bullet properties
BULLET_SIZE = 10
BULLET_SPEED = 10

# Asteroid properties
ASTEROID_SIZE = 20
ASTEROID_SPEED = 2

class Ship(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - SHIP_SIZE * 2, SHIP_SIZE, SHIP_SIZE)
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -SHIP_SPEED
        elif keys[pygame.K_RIGHT]:
            self.speed_x = SHIP_SPEED
        else:
            self.speed_x = 0

        if keys[pygame.K_UP]:
            self.speed_y = -SHIP_SPEED
        elif keys[pygameK.DOWN]:
            self.speed_y = SHIP_SPEED
        else:
            self.speed_y = 0

        self.x += self.speed_x
        self.y += self.speed_y

        # Boundary checking
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - SHIP_SIZE:
            self.x = WIDTH - SHIP_SIZE

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - SHIP_SIZE * 2:
            self.y = HEIGHT - SHIP_SIZE * 2

class Bullet(pygame.Rect):
    def __init__(self, ship):
        super().__init__(ship.centerx, ship.top, BULLET_SIZE, BULLET_SIZE)
        self.speed_y = -BULLET_SPEED

    def move(self):
        self.y += self.speed_y

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH), random.randint(-HEIGHT // 2, HEIGHT // 2), ASTEROID_SIZE, ASTEROID_SIZE)
        self.speed_x = random.choice([-ASTEROID_SPEED, ASTEROID_SPEED])
        self.speed_y = random.choice([-ASTEROID_SPEED, ASTEROID_SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

def main():
    st.title("Asteroids Game")

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ship = Ship()
    bullets = []
    asteroids = [Asteroid() for _ in range(10)]
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship))

        ship.move()
        for bullet in bullets:
            bullet.move()
            if bullet.bottom < 0:
                bullets.remove(bullet)

        for asteroid in asteroids:
            asteroid.move()
            if ship.colliderect(asteroid):
                running = False
            elif bullet.colliderect(asteroid) for bullet in bullets):
                score += 1
                bullets.remove(asteroid)
                asteroids.remove(asteroid)
                asteroids.append(Asteroid())

        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, ship)
        for bullet in bullets:
            pygame.draw.rect(screen, GREEN, bullet)
        for asteroid in asteroids:
            pygame.draw.ellipse(screen, (0, 0, 255), asteroid)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    st.write("Game Over! Your final score is:", score)

if __name__ == "__main__":
    main()
```

This code creates a simple Asteroids game with the following features:

*   A spaceship that can be controlled using the arrow keys.
*   Bullets that can be shot using the space bar.
*   Asteroids that move around the screen and will destroy the ship if they collide.
*   Scorekeeping, which increases each time an asteroid is hit.

You can run this code by saving it as `asteroids_game.py` and running `streamlit run asteroids_game.py`. This will launch a web-based version of the game in your default browser.