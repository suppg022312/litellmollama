Certainly! Below is a simple implementation of the Space Invaders game using Python and Pygame. Make sure you have Pygame installed on your system. If not, you can install it using pip:

```sh
pip install pygame
```

Here's the code for the Space Invaders game:

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player settings
player_img = pygame.image.load('player.png')
player_width = 64
player_height = 64
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Enemy settings
enemy_img = pygame.image.load('enemy.png')
enemy_width = 64
enemy_height = 64
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(50, 200)
enemy_speed = 3
enemy_list = []
num_enemies = 5

# Bullet settings
bullet_img = pygame.image.load('bullet.png')
bullet_width = 32
bullet_height = 32
bullet_x = 0
bullet_y = screen_height - player_height - 10
bullet_speed = 7
bullet_state = "ready"  # "ready" - can't see bullet on the screen, "fire" - bullet is currently moving

# Functions to draw images on the screen
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))  # Adjust the position to look like it's coming from the player

# Main game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + 16  # Adjust the position to look like it's coming from the player
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - player_width:
        player_x = screen_width - player_width

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y >= screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(50, 200)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"

    # Draw player, enemy, and bullet
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()

pygame.quit()
```

### Notes:
1. **Image Files**: You need to have three image files (`player.png`, `enemy.png`, and `bullet.png`) in the same directory as your script.
2. **Player Movement**: Use the left and right arrow keys to move the player.
3. **Shooting**: Press the spacebar to shoot a bullet.
4. **Game Loop**: The game loop handles events, updates positions, draws images, and checks for collisions.

This is a basic implementation of Space Invaders. You can extend it by adding collision detection, scoring, levels, and more advanced graphics.