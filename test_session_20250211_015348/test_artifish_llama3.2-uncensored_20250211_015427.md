# Model Response: artifish/llama3.2-uncensored
Generated on: 2025-02-11 01:54:27


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
**Asteroid Game in Python using Pygame**

**Game Description:**
This is a simple implementation of an asteroid game where you control a spaceship and destroy incoming asteroids. The game ends when the spaceship collides with an asteroid.

**Code:**

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Spaceship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT - 50
        self.speed_x = 0
        self.speed_y = 0

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 30, 30))

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(1, 2)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 30, 30))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = -5

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 10, 10))

def main():
    clock = pygame.time.Clock()
    spaceship = Spaceship()
    asteroids = [Asteroid() for _ in range(10)]
    bullets = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(spaceship.x + 15, spaceship.y - 15))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship.speed_x = -5
        elif keys[pygame.K_RIGHT]:
            spaceship.speed_x = 5
        else:
            spaceship.speed_x = 0

        if keys[pygame.K_UP]:
            spaceship.speed_y = -5
        elif keys[pygame.K_DOWN]:
            spaceship.speed_y = 5
        else:
            spaceship.speed_y = 0

        # Move the spaceship
        spaceship.x += spaceship.speed_x
        spaceship.y += spaceship.speed_y

        # Move the asteroids
        for asteroid in asteroids:
            asteroid.x += asteroid.speed_x
            asteroid.y += asteroid.speed_y

            # Check if the asteroid is off the screen
            if asteroid.y > HEIGHT or asteroid.y < -HEIGHT:
                asteroids.remove(asteroid)
                continue

            # Check if the spaceship has collided with an asteroid
            if (abs(asteroid.x - spaceship.x) < 30 and abs(asteroid.y - spaceship.y) < 30):
                print("Game Over")
                pygame.quit()
                sys.exit()

        # Move the bullets
        for bullet in bullets:
            bullet.x += bullet.speed_x
            bullet.y += bullet.speed_y

            # Check if the bullet has hit an asteroid
            for asteroid in asteroids[:]:
                if (abs(bullet.x - asteroid.x) < 10 and abs(bullet.y - asteroid.y) < 10):
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)

            # Check if the bullet has gone off the screen
            if bullet.y > HEIGHT:
                bullets.remove(bullet)

        # Create new asteroids
        if random.random() < 0.1:
            asteroids.append(Asteroid())

        # Draw everything
        screen.fill((0, 0, 0))
        spaceship.draw()
        for asteroid in asteroids:
            asteroid.draw()
        for bullet in bullets:
            bullet.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```
</div>

**How to Run:**
To run the game, save this code in a file with a `.py` extension and run it using Python. Make sure you have Pygame installed before running the code.

**Gameplay:**
Use the arrow keys to move the spaceship left, right, up, or down. Press the space bar to fire bullets at the asteroids. The game ends when the spaceship collides with an asteroid.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: artifish/llama3.2-uncensored
# Timestamp: 2025-02-11 01:54:27


```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: artifish/llama3.2-uncensored
- Timestamp: 2025-02-11 01:54:27
- File: test_artifish_llama3.2-uncensored_20250211_015427.md
