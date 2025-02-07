# Model Response: deepseek-coder-v2
Generated on: 2025-02-07 20:30:44


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
 Creating a simple Asteroids-like game in Python can be an engaging project, especially if you're using libraries like `pygame` for graphics and sound. Below is a basic example to get you started. This script will create a window where the player can move a spaceship around with arrow keys and shoot bullets at asteroids that move randomly.

First, make sure you have `pygame` installed. You can install it using pip:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```bash
pip install pygame
```
</div>

Here's a basic implementation of an Asteroids-like game in Python using `pygame`:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [width // 2, height // 2]

# Bullet settings
bullet_speed = 10
bullet_life = 60
bullets = []

# Asteroid settings
asteroid_size = 30
asteroid_speeds = list(range(1, 5))
asteroids = []

def draw_player():
    pygame.draw.circle(screen, WHITE, player_pos, player_size)

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, RED, bullet['pos'], 3)
        bullet['life'] -= 1
        if bullet['life'] <= 0:
            bullets.remove(bullet)

def move_bullets():
    for bullet in bullets:
        bullet['pos'][0] += bullet_speed * (bullet['dir'] == 'right') - bullet_speed * (bullet['dir'] == 'left')
        bullet['pos'][1] += bullet_speed * (bullet['dir'] == 'down') - bullet_speed * (bullet['dir'] == 'up')

def draw_asteroids():
    for asteroid in asteroids:
        pygame.draw.circle(screen, WHITE, asteroid['pos'], asteroid_size)

def move_asteroids():
    for asteroid in asteroids:
        asteroid['pos'][0] += random.choice(asteroid_speeds) * (random.randint(0, 1) == 0) - random.choice(asteroid_speeds) * (random.randint(0, 1) == 1)
        asteroid['pos'][1] += random.choice(asteroid_speeds) * (random.randint(0, 1) == 0) - random.choice(asteroid_speeds) * (random.randint(0, 1) == 1)

def check_collision():
    for bullet in bullets:
        for asteroid in asteroids:
            if pygame.math.Vector2(bullet['pos']).distance_to(pygame.math.Vector2(asteroid['pos'])) < player_size + asteroid_size:
                bullets.remove(bullet)
                asteroids.remove(asteroid)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append({'pos': list(player_pos), 'dir': {'left': -1, 'right': 1, 'up': 0, 'down': 0}[pygame.key.get_pressed()[event.key]]})

        screen.fill(BLACK)

        draw_player()
        move_player()
        draw_bullets()
        move_bullets()
        draw_asteroids()
        move_asteroids()
        check_collision()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
```
</div>

This script sets up a basic game loop where the player can move around with arrow keys and shoot bullets by pressing space. The asteroids move randomly, and you have to avoid collisions between them and your bullets.

You can expand this base code by adding more features like scoring, different types of asteroids, power-ups, etc.

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: deepseek-coder-v2
# Timestamp: 2025-02-07 20:30:44

pip install pygame


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [width // 2, height // 2]

# Bullet settings
bullet_speed = 10
bullet_life = 60
bullets = []

# Asteroid settings
asteroid_size = 30
asteroid_speeds = list(range(1, 5))
asteroids = []

def draw_player():
    pygame.draw.circle(screen, WHITE, player_pos, player_size)

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, RED, bullet['pos'], 3)
        bullet['life'] -= 1
        if bullet['life'] <= 0:
            bullets.remove(bullet)

def move_bullets():
    for bullet in bullets:
        bullet['pos'][0] += bullet_speed * (bullet['dir'] == 'right') - bullet_speed * (bullet['dir'] == 'left')
        bullet['pos'][1] += bullet_speed * (bullet['dir'] == 'down') - bullet_speed * (bullet['dir'] == 'up')

def draw_asteroids():
    for asteroid in asteroids:
        pygame.draw.circle(screen, WHITE, asteroid['pos'], asteroid_size)

def move_asteroids():
    for asteroid in asteroids:
        asteroid['pos'][0] += random.choice(asteroid_speeds) * (random.randint(0, 1) == 0) - random.choice(asteroid_speeds) * (random.randint(0, 1) == 1)
        asteroid['pos'][1] += random.choice(asteroid_speeds) * (random.randint(0, 1) == 0) - random.choice(asteroid_speeds) * (random.randint(0, 1) == 1)

def check_collision():
    for bullet in bullets:
        for asteroid in asteroids:
            if pygame.math.Vector2(bullet['pos']).distance_to(pygame.math.Vector2(asteroid['pos'])) < player_size + asteroid_size:
                bullets.remove(bullet)
                asteroids.remove(asteroid)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append({'pos': list(player_pos), 'dir': {'left': -1, 'right': 1, 'up': 0, 'down': 0}[pygame.key.get_pressed()[event.key]]})

        screen.fill(BLACK)

        draw_player()
        move_player()
        draw_bullets()
        move_bullets()
        draw_asteroids()
        move_asteroids()
        check_collision()

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
- Model: deepseek-coder-v2
- Timestamp: 2025-02-07 20:30:44
- File: test_deepseek-coder-v2_20250207_203044.md
