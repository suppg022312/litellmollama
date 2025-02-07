# Model Response: llama3.2-3b-instruct-fp16
Generated on: 2025-02-07 20:31:05


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

### Installation

To run this code, you'll need to install Pygame. You can do this with pip:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```bash
pip install pygame
```
</div>

### Code

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import math
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = math.pi / 4
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05
        if keys[pygame.K_UP]:
            self.speed_x += math.sin(self.angle) * 0.5
            self.speed_y -= math.cos(self.angle) * 0.5

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, (
            (self.x + math.cos(self.angle) * 20, self.y - math.sin(self.angle) * 20),
            (self.x + math.cos(self.angle - math.pi / 2) * 20, self.y + math.sin(self.angle - math.pi / 2) * 20),
            (self.x + math.cos(self.angle + math.pi / 2) * 20, self.y - math.sin(self.angle + math.pi / 2) * 20)
        ))

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 20)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ship = Ship()
    asteroids = [Asteroid() for _ in range(10)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        ship.move()
        ship.draw(screen)

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)
            if (ship.x - asteroid.x) ** 2 + (ship.y - asteroid.y) ** 2 < 100:
                print("Game Over")
                running = False

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
</div>

### Explanation

This code creates a simple Asteroids game where you control a ship with the arrow keys and try to avoid asteroids that move around the screen. If an asteroid collides with the ship, the game ends.

The `Ship` class represents the player's ship, which moves based on user input (left, right, up) and draws itself on the screen.

The `Asteroid` class represents the asteroids, which move randomly across the screen and draw themselves on the screen. If an asteroid collides with the ship, it prints "Game Over" to the console and ends the game.

In the main loop of the program, the game checks for user input, moves each object (ship and asteroids), draws everything on the screen, and limits the frame rate to 60 FPS using `pygame.time.Clock().tick(60)`.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2-3b-instruct-fp16
# Timestamp: 2025-02-07 20:31:05

pip install pygame


import pygame
import math
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Ship:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = math.pi / 4
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05
        if keys[pygame.K_UP]:
            self.speed_x += math.sin(self.angle) * 0.5
            self.speed_y -= math.cos(self.angle) * 0.5

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, (
            (self.x + math.cos(self.angle) * 20, self.y - math.sin(self.angle) * 20),
            (self.x + math.cos(self.angle - math.pi / 2) * 20, self.y + math.sin(self.angle - math.pi / 2) * 20),
            (self.x + math.cos(self.angle + math.pi / 2) * 20, self.y - math.sin(self.angle + math.pi / 2) * 20)
        ))

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 20)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    ship = Ship()
    asteroids = [Asteroid() for _ in range(10)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        ship.move()
        ship.draw(screen)

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)
            if (ship.x - asteroid.x) ** 2 + (ship.y - asteroid.y) ** 2 < 100:
                print("Game Over")
                running = False

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
- Model: llama3.2-3b-instruct-fp16
- Timestamp: 2025-02-07 20:31:05
- File: test_llama3.2-3b-instruct-fp16_20250207_203105.md
