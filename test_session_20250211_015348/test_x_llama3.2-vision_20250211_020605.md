# Model Response: x/llama3.2-vision
Generated on: 2025-02-11 02:06:05


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
create me a python based asteroid game 

```
</div>

## Model Solution
Here is a simple implementation of an Asteroid game using Python and the Pygame library.

**Asteroids Game**
=====================

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH), random.randint(-HEIGHT // 2, 0),
                         random.randint(20, 50), random.randint(10, 30))
        self.speed_x = random.choice([-1, 1]) * random.randint(1, 5)
        self.speed_y = random.randint(1, 3)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Ship(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH // 2, HEIGHT - 50, 30, 20)
        self.speed = 5

    def move_up(self):
        if self.top > 0:
            self.y -= self.speed
        else:
            self.y = 0

    def move_down(self):
        if self.bottom < HEIGHT:
            self.y += self.speed
        else:
            self.y = HEIGHT - self.height

class Bullet(pygame.Rect):
    def __init__(self, ship):
        super().__init__(ship.centerx, ship.top, 5, 10)
        self.speed_y = -15

    def move(self):
        self.y += self.speed_y

def main():
    clock = pygame.time.Clock()
    ship = Ship()
    asteroids = [Asteroid() for _ in range(10)]
    bullets = []
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ship.move_up()
        if keys[pygame.K_DOWN]:
            ship.move_down()

        screen.fill(BLACK)
        for asteroid in asteroids:
            asteroid.move()
            pygame.draw.ellipse(screen, WHITE, asteroid)
            if asteroid.bottom > HEIGHT:
                asteroids.remove(asteroid)
                asteroids.append(Asteroid())
            elif ship.colliderect(asteroid):
                print("Game Over")
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            bullet.move()
            pygame.draw.rect(screen, WHITE, bullet)
            if bullet.bottom < 0:
                bullets.remove(bullet)

        pygame.draw.rect(screen, WHITE, ship)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        for asteroid in asteroids:
            if asteroid.colliderect(ship):
                print("Game Over")
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```
</div>

This code creates a simple Asteroids game where the player controls a ship at the bottom of the screen. The goal is to avoid asteroids that are falling from the top of the screen and shoot bullets using the space bar. If an asteroid hits the ship, the game ends.

Note: This is a very basic implementation and there's plenty of room for improvement (e.g., smoother animations, more realistic physics, etc.).

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: x/llama3.2-vision
# Timestamp: 2025-02-11 02:06:05

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH), random.randint(-HEIGHT // 2, 0),
                         random.randint(20, 50), random.randint(10, 30))
        self.speed_x = random.choice([-1, 1]) * random.randint(1, 5)
        self.speed_y = random.randint(1, 3)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Ship(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH // 2, HEIGHT - 50, 30, 20)
        self.speed = 5

    def move_up(self):
        if self.top > 0:
            self.y -= self.speed
        else:
            self.y = 0

    def move_down(self):
        if self.bottom < HEIGHT:
            self.y += self.speed
        else:
            self.y = HEIGHT - self.height

class Bullet(pygame.Rect):
    def __init__(self, ship):
        super().__init__(ship.centerx, ship.top, 5, 10)
        self.speed_y = -15

    def move(self):
        self.y += self.speed_y

def main():
    clock = pygame.time.Clock()
    ship = Ship()
    asteroids = [Asteroid() for _ in range(10)]
    bullets = []
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ship.move_up()
        if keys[pygame.K_DOWN]:
            ship.move_down()

        screen.fill(BLACK)
        for asteroid in asteroids:
            asteroid.move()
            pygame.draw.ellipse(screen, WHITE, asteroid)
            if asteroid.bottom > HEIGHT:
                asteroids.remove(asteroid)
                asteroids.append(Asteroid())
            elif ship.colliderect(asteroid):
                print("Game Over")
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            bullet.move()
            pygame.draw.rect(screen, WHITE, bullet)
            if bullet.bottom < 0:
                bullets.remove(bullet)

        pygame.draw.rect(screen, WHITE, ship)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        for asteroid in asteroids:
            if asteroid.colliderect(ship):
                print("Game Over")
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

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
- Model: x/llama3.2-vision
- Timestamp: 2025-02-11 02:06:05
- File: test_x_llama3.2-vision_20250211_020605.md
