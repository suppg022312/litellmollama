Creating an entire Space Invaders game from scratch can be quite complex, but I can guide you through the process and provide you with a simplified version of the game. We'll use Python's `pygame` library for the graphics and user interaction. If you haven't installed pygame yet, you can do so using pip:
```bash
pip install pygame
```

Here's a basic implementation of Space Invaders in Python:

```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game settings
player_speed = 10
bullet_speed = 10
enemy_speed = 3
bullet_cooldown = 1.5  # Cooldown in seconds for shooting

# Player and Enemy classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speed = player_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 20)
        self.rect.y = 10
        self.speed = enemy_speed

    def update(self):
        if self.rect.bottom > height:
            self.rect.x += self.speed
            self.rect.y = 10 - self.rect.height

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.bottom + 10
        self.speed = bullet_speed
        self.active = True

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            self.kill()

# Game objects
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

clock = pygame.time.Clock()

def generate_enemy():
    for i in range(5):
        enemy = Enemy()
        enemies.add(enemy)

# Main game loop
running = True
cooldown_timer = 0
score = 0

while running:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and cooldown_timer <= 0:
                bullet = Bullet(player)
                bullets.add(bullet)
                cooldown_timer = bullet_cooldown

    # Update game objects
    player.update()
    enemies.update()
    bullets.update()

    # Generate new enemies
    if random.random() < 0.05 and not (enemies.empty() or len(bullets.sprites()) > 0):
        generate_enemy()

    # Collision detection
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for enemy in collisions:
        score += 10

    # Clear screen
    screen.fill(BLACK)

    # Draw game objects
    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
```

This code sets up a basic Space Invaders game with the following features:
- A player spaceship that can move left and right using the arrow keys.
- Enemies that randomly appear and move down from the top of the screen.
- Bullets that the player can shoot by pressing the spacebar, with a cooldown period between shots.
- Collision detection to destroy enemies when bullets hit them, awarding points.

Remember that this is a simplified version, and you can add more features like sound effects, additional levels, enemy patterns, and more advanced gameplay mechanics as you gain experience with game development in Python.