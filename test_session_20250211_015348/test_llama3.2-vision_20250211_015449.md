# Model Response: llama3.2-vision
Generated on: 2025-02-11 01:54:49


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
Here is a simple Python-based Asteroid game using Pygame library.

**Asteroid Game Code**
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - 50, 30, 30)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed_y
        if keys[pygame.K_DOWN]:
            self.y += self.speed_y
        if keys[pygame.K_LEFT]:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.x += self.speed_x

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self)

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH), random.randint(-HEIGHT // 2, HEIGHT // 2), 30, 30)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(1, 10)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < -HEIGHT // 2 or self.y > HEIGHT // 2:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self)

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 20)
        self.speed_y = -15

    def move(self):
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self)

def main():
    pygame.init()
    pygame.display.set_caption('Asteroid Game')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    asteroids = [Asteroid() for _ in range(10)]
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.centerx, player.top))

        screen.fill(BLACK)
        player.move()
        player.draw(screen)

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)
            if asteroid.colliderect(player):
                print("Game Over!")
                running = False

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)
            for asteroid in asteroids:
                if bullet.colliderect(asteroid):
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
</div>

**How to Play**

* Use the arrow keys to move your ship.
* Press space bar to shoot a bullet.
* Destroy asteroids by hitting them with bullets.
* Avoid getting hit by asteroids.

Note: This is a simple game and there's no scoring system or level design. You can enhance it as per your requirements.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2-vision
# Timestamp: 2025-02-11 01:54:49

import pygame
import random
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - 50, 30, 30)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed_y
        if keys[pygame.K_DOWN]:
            self.y += self.speed_y
        if keys[pygame.K_LEFT]:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.x += self.speed_x

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self)

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH), random.randint(-HEIGHT // 2, HEIGHT // 2), 30, 30)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(1, 10)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < -HEIGHT // 2 or self.y > HEIGHT // 2:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self)

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 20)
        self.speed_y = -15

    def move(self):
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self)

def main():
    pygame.init()
    pygame.display.set_caption('Asteroid Game')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    asteroids = [Asteroid() for _ in range(10)]
    bullets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.centerx, player.top))

        screen.fill(BLACK)
        player.move()
        player.draw(screen)

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)
            if asteroid.colliderect(player):
                print("Game Over!")
                running = False

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)
            for asteroid in asteroids:
                if bullet.colliderect(asteroid):
                    asteroids.remove(asteroid)
                    bullets.remove(bullet)

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
- Model: llama3.2-vision
- Timestamp: 2025-02-11 01:54:49
- File: test_llama3.2-vision_20250211_015449.md
