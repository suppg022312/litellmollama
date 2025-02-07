# Model Response: llama3.2
Generated on: 2025-02-07 20:31:56


<style>
.copy-button {
    position: absolute;
    top: 5px;
    right: 5px;
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    z-index: 1;
}
.code-container {
    position: relative;
    margin: 10px 0;
}
.copy-button:hover {
    background-color: #45a049;
}
.copy-button:active {
    background-color: #3d8b40;
}
</style>

<script>
function copyCode(buttonElement) {
    const codeBlock = buttonElement.parentElement.querySelector('code');
    const range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    try {
        document.execCommand('copy');
        buttonElement.textContent = 'Copied!';
        setTimeout(() => {
            buttonElement.textContent = 'Copy';
        }, 2000);
    } catch(e) {
        console.error('Failed to copy text:', e);
        buttonElement.textContent = 'Failed to copy';
    }
    window.getSelection().removeAllRanges();
}
</script>


## Original Task
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```
python asteroids game

```
</div>

## Model Solution
Here's a simple implementation of the classic Asteroids game using Python and the Pygame library.

**Asteroids Game Code**
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2
BULLET_SPEED = 5
ASTEROID_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = 0
        self.speed = SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed * math.sin(math.radians(self.angle))
        if keys[pygame.K_DOWN]:
            self.y += self.speed * math.sin(math.radians(self.angle))
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * -math.cos(math.radians(self.angle))
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * -math.cos(math.radians(self.angle))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self):
        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * -math.cos(math.radians(self.angle))

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = ASTEROID_SIZE

def main():
    clock = pygame.time.Clock()
    ship = Ship()
    bullets = []
    asteroids = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship.x, ship.y))

        # Move the ship
        ship.move()

        # Move the bullets
        for bullet in bullets:
            bullet.move()
            if bullet.y < 0 or bullet.y > HEIGHT - ASTEROID_SIZE:
                bullets.remove(bullet)

        # Move the asteroids
        for asteroid in asteroids:
            asteroid.x += math.sin(math.radians(asteroid.angle)) * 1
            asteroid.y -= math.cos(math.radians(asteroid.angle)) * 1

        # Add new asteroids
        if random.random() < 0.05:
            asteroids.append(Asteroid(WIDTH, HEIGHT))

        # Check for collisions
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                dx = asteroid.x - bullet.x
                dy = asteroid.y - bullet.y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < ASTEROID_SIZE / 2:
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)

        # Check for ship collisions with asteroids
        for asteroid in asteroids[:]:
            dx = ship.x - asteroid.x
            dy = ship.y - asteroid.y
            distance = math.sqrt(dx * dx + dy * dy)
            if distance < ASTEROID_SIZE:
                running = False

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (int(ship.x), int(ship.y)), 10)

        for bullet in bullets:
            pygame.draw.rect(screen, RED, (int(bullet.x - math.sin(math.radians(bullet.angle)) * ASTEROID_SIZE / 2),
                                           int(bullet.y + math.cos(math.radians(bullet.angle)) * ASTEROID_SIZE / 2),
                                           ASTEROID_SIZE, ASTEROID_SIZE))
        for asteroid in asteroids:
            pygame.draw.circle(screen, RED, (int(asteroid.x), int(asteroid.y)), ASTEROID_SIZE)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
</div>

**How to Play**

1. Run the code using Python.
2. Use the arrow keys to control the ship.
3. Press the space bar to fire a bullet.
4. Avoid colliding with asteroids and bullets.

Note: This is a basic implementation of the game, and there's room for improvement. You can add features like scorekeeping, power-ups, and smoother animations to make the game more engaging.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2
# Timestamp: 2025-02-07 20:31:56

import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2
BULLET_SPEED = 5
ASTEROID_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = 0
        self.speed = SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed * math.sin(math.radians(self.angle))
        if keys[pygame.K_DOWN]:
            self.y += self.speed * math.sin(math.radians(self.angle))
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * -math.cos(math.radians(self.angle))
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * -math.cos(math.radians(self.angle))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self):
        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * -math.cos(math.radians(self.angle))

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = ASTEROID_SIZE

def main():
    clock = pygame.time.Clock()
    ship = Ship()
    bullets = []
    asteroids = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship.x, ship.y))

        # Move the ship
        ship.move()

        # Move the bullets
        for bullet in bullets:
            bullet.move()
            if bullet.y < 0 or bullet.y > HEIGHT - ASTEROID_SIZE:
                bullets.remove(bullet)

        # Move the asteroids
        for asteroid in asteroids:
            asteroid.x += math.sin(math.radians(asteroid.angle)) * 1
            asteroid.y -= math.cos(math.radians(asteroid.angle)) * 1

        # Add new asteroids
        if random.random() < 0.05:
            asteroids.append(Asteroid(WIDTH, HEIGHT))

        # Check for collisions
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                dx = asteroid.x - bullet.x
                dy = asteroid.y - bullet.y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance < ASTEROID_SIZE / 2:
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)

        # Check for ship collisions with asteroids
        for asteroid in asteroids[:]:
            dx = ship.x - asteroid.x
            dy = ship.y - asteroid.y
            distance = math.sqrt(dx * dx + dy * dy)
            if distance < ASTEROID_SIZE:
                running = False

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (int(ship.x), int(ship.y)), 10)

        for bullet in bullets:
            pygame.draw.rect(screen, RED, (int(bullet.x - math.sin(math.radians(bullet.angle)) * ASTEROID_SIZE / 2),
                                           int(bullet.y + math.cos(math.radians(bullet.angle)) * ASTEROID_SIZE / 2),
                                           ASTEROID_SIZE, ASTEROID_SIZE))
        for asteroid in asteroids:
            pygame.draw.circle(screen, RED, (int(asteroid.x), int(asteroid.y)), ASTEROID_SIZE)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: llama3.2
- Timestamp: 2025-02-07 20:31:56
- File: test_llama3.2_20250207_203156.md
