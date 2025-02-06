Creating a full Space Invaders game can be quite complex and lengthy, but I'll provide you with a simplified version of the game using Python's `pygame` library. This basic implementation will include player movement, shooting, enemy (alien) spawning, and collision detection.

Firstly, ensure you have `pygame` installed. You can install it via pip if you haven't already:

```bash
pip install pygame
```

Here is a simple version of Space Invaders in Python using Pygame:

```python
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions and colors
screen_width = 800
screen_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# Screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Player settings
player_speed = 5
player_size_x = 64
player_size_y = 64

# Enemy settings
enemy_speed = 3
enemy_spawn_rate = 100 # lower means more frequent spawning

# Bullet settings
bullet_speed = -10
bullet_width = 3
bullet_height = 15

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_size_x, player_size_y))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2 - player_size_x // 2
        self.rect.y = screen_height - player_size_y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += player_speed
    
    def shoot(self):
        bullet = Bullet(player=self)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)

    def update(self):
        if self.rect.bottom >= 0:
            self.rect.y += enemy_speed
            if random.randint(1, enemy_spawn_rate) == 1:
                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemies.add(new_enemy)
        else:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player=None):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        if player is not None:
            self.rect.midtop = player.rect.midtop

    def update(self):
        self.rect.y += bullet_speed
        if self.rect.bottom < 0 or pygame.sprite.spritecollideany(self, enemies):
            self.kill()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()

    all_sprites.update()
    
    # Collision detection between bullets and enemies
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
```

This code sets up a basic game structure for Space Invaders. You have player movement left and right with the ability to shoot by pressing the spacebar. Enemies (aliens) are randomly spawned from above, moving downwards.

**Note:**
- This is a very basic version of Space Invaders without detailed graphics or sound effects.
- The game logic could be extended for more advanced features like different levels, scoring system, and enemy patterns.
- To enhance the game further, consider adding sprites (images) instead of simple rectangles for characters and backgrounds.

This should get you started with a simple Python-based space shooter using Pygame!