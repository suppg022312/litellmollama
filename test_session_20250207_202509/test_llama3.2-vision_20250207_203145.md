# Model Response: llama3.2-vision
Generated on: 2025-02-07 20:31:45


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
Here's a simple implementation of an Asteroids game using Python and the Pygame library.

**Game Description:**
The player controls a spaceship that can move left, right, up, and down. The goal is to destroy as many asteroids as possible while avoiding collision with them. Each asteroid destroyed earns points.

**Code:**

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import sys
import random

# Game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACESHIP_SIZE = 50
ASTEROID_SIZE = 20
SPEED = 5
BULLET_SPEED = 10
SCORE_FONT = None
LIVES_FONT = None
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Spaceship(pygame.Rect):
    def __init__(self):
        super().__init__(SCREEN_WIDTH / 2, SCREEN_HEIGHT - SPACESHIP_SIZE * 2, SPACESHIP_SIZE, SPACESHIP_SIZE)
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - SPACESHIP_SIZE:
            self.x = SCREEN_WIDTH - SPACESHIP_SIZE

        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - SPACESHIP_SIZE * 2:
            self.y = SCREEN_HEIGHT - SPACESHIP_SIZE * 2

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE), random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE), ASTEROID_SIZE, ASTEROID_SIZE)
        self.speed_x = random.choice([-SPEED, SPEED])
        self.speed_y = random.choice([-SPEED, SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 5)
        self.speed_y = -BULLET_SPEED

    def move(self):
        self.y += self.speed_y

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main():
    global SCORE_FONT
    global LIVES_FONT

    score = 0
    lives = 3

    spaceship = Spaceship()
    asteroids = [Asteroid() for _ in range(5)]
    bullets = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < 10:
                    bullets.append(Bullet(spaceship.centerx, spaceship.top))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            spaceship.speed_x = -SPEED
        elif keys[pygame.K_RIGHT]:
            spaceship.speed_x = SPEED
        else:
            spaceship.speed_x = 0

        if keys[pygame.K_UP]:
            spaceship.speed_y = -SPEED
        elif keys[pygame.K_DOWN]:
            spaceship.speed_y = SPEED
        else:
            spaceship.speed_y = 0

        spaceship.move()

        for asteroid in asteroids:
            asteroid.move()
            if asteroid.colliderect(spaceship):
                lives -= 1
                asteroids.remove(asteroid)
                asteroid.x = random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE)
                asteroid.y = random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE)

        for bullet in bullets:
            bullet.move()
            if bullet.y < 0:
                bullets.remove(bullet)
            else:
                for asteroid in asteroids:
                    if bullet.colliderect(asteroid):
                        score += 1
                        asteroids.remove(asteroid)
                        bullets.remove(bullet)
                        asteroid.x = random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE)
                        asteroid.y = random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE)

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, WHITE, spaceship)

        for asteroid in asteroids:
            pygame.draw.ellipse(screen, RED, asteroid)

        for bullet in bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)

        draw_text("Score: " + str(score), SCORE_FONT, WHITE, screen, 10, 10)
        draw_text("Lives: " + str(lives), LIVES_FONT, WHITE, screen, SCREEN_WIDTH - 150, 10)

        pygame.display.flip()

        clock.tick(60)

        if lives <= 0:
            break

    print("Game Over! Final score:", score)
    pygame.quit()

if __name__ == "__main__":
    SCORE_FONT = pygame.font.SysFont('Arial', 20)
    LIVES_FONT = pygame.font.SysFont('Arial', 20)
    main()
```
</div>

This code will create a window with a spaceship at the bottom. You can move the spaceship using the arrow keys, and fire bullets using the space bar. The goal is to destroy as many asteroids as possible while avoiding collision with them.

Note that this is just one way to implement an Asteroids game in Python. There are many variations and improvements you could make to this code.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: llama3.2-vision
# Timestamp: 2025-02-07 20:31:45

import pygame
import sys
import random

# Game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACESHIP_SIZE = 50
ASTEROID_SIZE = 20
SPEED = 5
BULLET_SPEED = 10
SCORE_FONT = None
LIVES_FONT = None
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Spaceship(pygame.Rect):
    def __init__(self):
        super().__init__(SCREEN_WIDTH / 2, SCREEN_HEIGHT - SPACESHIP_SIZE * 2, SPACESHIP_SIZE, SPACESHIP_SIZE)
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - SPACESHIP_SIZE:
            self.x = SCREEN_WIDTH - SPACESHIP_SIZE

        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - SPACESHIP_SIZE * 2:
            self.y = SCREEN_HEIGHT - SPACESHIP_SIZE * 2

class Asteroid(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE), random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE), ASTEROID_SIZE, ASTEROID_SIZE)
        self.speed_x = random.choice([-SPEED, SPEED])
        self.speed_y = random.choice([-SPEED, SPEED])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 5)
        self.speed_y = -BULLET_SPEED

    def move(self):
        self.y += self.speed_y

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main():
    global SCORE_FONT
    global LIVES_FONT

    score = 0
    lives = 3

    spaceship = Spaceship()
    asteroids = [Asteroid() for _ in range(5)]
    bullets = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets) < 10:
                    bullets.append(Bullet(spaceship.centerx, spaceship.top))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            spaceship.speed_x = -SPEED
        elif keys[pygame.K_RIGHT]:
            spaceship.speed_x = SPEED
        else:
            spaceship.speed_x = 0

        if keys[pygame.K_UP]:
            spaceship.speed_y = -SPEED
        elif keys[pygame.K_DOWN]:
            spaceship.speed_y = SPEED
        else:
            spaceship.speed_y = 0

        spaceship.move()

        for asteroid in asteroids:
            asteroid.move()
            if asteroid.colliderect(spaceship):
                lives -= 1
                asteroids.remove(asteroid)
                asteroid.x = random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE)
                asteroid.y = random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE)

        for bullet in bullets:
            bullet.move()
            if bullet.y < 0:
                bullets.remove(bullet)
            else:
                for asteroid in asteroids:
                    if bullet.colliderect(asteroid):
                        score += 1
                        asteroids.remove(asteroid)
                        bullets.remove(bullet)
                        asteroid.x = random.randint(0, SCREEN_WIDTH - ASTEROID_SIZE)
                        asteroid.y = random.randint(0, SCREEN_HEIGHT / 2 - ASTEROID_SIZE)

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, WHITE, spaceship)

        for asteroid in asteroids:
            pygame.draw.ellipse(screen, RED, asteroid)

        for bullet in bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)

        draw_text("Score: " + str(score), SCORE_FONT, WHITE, screen, 10, 10)
        draw_text("Lives: " + str(lives), LIVES_FONT, WHITE, screen, SCREEN_WIDTH - 150, 10)

        pygame.display.flip()

        clock.tick(60)

        if lives <= 0:
            break

    print("Game Over! Final score:", score)
    pygame.quit()

if __name__ == "__main__":
    SCORE_FONT = pygame.font.SysFont('Arial', 20)
    LIVES_FONT = pygame.font.SysFont('Arial', 20)
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
- Timestamp: 2025-02-07 20:31:45
- File: test_llama3.2-vision_20250207_203145.md
