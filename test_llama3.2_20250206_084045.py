Here's a simple implementation of the classic arcade game Space Invaders using Python and the Pygame library.

```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
BULLET_SIZE = 10
ENEMY_SIZE = 30
SPEED = 2

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player class
class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - PLAYER_SIZE * 2, PLAYER_SIZE, PLAYER_SIZE)
        self.speed_x = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed_x
        if keys[pygame.K_RIGHT] and self.x < WIDTH - PLAYER_SIZE:
            self.x += self.speed_x

# Bullet class
class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_SIZE, BULLET_SIZE)
        self.speed = SPEED

    def move(self):
        self.y -= self.speed

# Enemy class
class Enemy(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)

    def move(self):
        self.y += SPEED

# Game class
class SpaceInvaders:
    def __init__(self):
        self.player = Player()
        self.bullets = []
        self.enemies = [Enemy() for _ in range(10)]
        self.score = 0

    def draw(self):
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, self.player)
        for bullet in self.bullets:
            pygame.draw.rect(screen, (0, 255, 0), bullet)
        for enemy in self.enemies:
            pygame.draw.rect(screen, (128, 0, 128), enemy)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.x > 0:
            self.player.x -= self.player.speed_x
        if keys[pygame.K_RIGHT] and self.player.x < WIDTH - PLAYER_SIZE:
            self.player.x += self.player.speed_x

        for bullet in self.bullets[:]:
            if bullet.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.move()
                for enemy in self.enemies[:]:
                    if bullet.colliderect(enemy):
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.score += 1
        for enemy in self.enemies[:]:
            if enemy.y > HEIGHT:
                self.enemies.remove(enemy)
                continue
            enemy.move()
            if enemy.y < 0 or enemy.y > HEIGHT - ENEMY_SIZE * 2:
                self.enemies.remove(enemy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not any(b.y < 0 for b in self.bullets):
                    self.bullets.append(Bullet(self.player.x + PLAYER_SIZE // 2, self.player.top))

# Create the game instance
game = SpaceInvaders()

# Main loop
while True:
    game.handle_events()
    game.update()
    game.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
```

This code creates a window with a player that can be controlled using the left and right arrow keys. The player shoots bullets by pressing the space bar, which move up the screen at a constant speed. Enemies move down the screen at a faster speed than the bullets, and when an enemy is hit by a bullet, it disappears and the score increases. If an enemy reaches the bottom of the screen, it also disappears.

Please note that this code does not include any win or lose conditions, but you can add those yourself as needed.