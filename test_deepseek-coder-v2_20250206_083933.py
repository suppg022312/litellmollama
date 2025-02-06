 Creating a simple Space Invaders game in Python can be a fun project. Below is a basic implementation using the Pygame library, which is commonly used for building games in Python. If you don't have Pygame installed, you can install it using pip:

```sh
pip install pygame
```

Here's a simple Space Invaders game:

```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_width = 100
player_height = 10
player_speed = 5

# Enemy settings
enemy_width = 40
enemy_height = 30
enemy_color = RED
enemy_list = []
enemy_rows = 5
enemy_cols = 10
enemy_gap = 20

# Bullet settings
bullet_speed = 10
bullet_radius = 5
bullet_fired = False
bullet_x, bullet_y = -100, -100

# Set up the player
player_x = (WIDTH // 2) - (player_width // 2)
player_y = HEIGHT - player_height - 10

# Function to create enemies
def create_enemies():
    for row in range(enemy_rows):
        for col in range(enemy_cols):
            enemy_x = col * (enemy_width + enemy_gap) + 20
            enemy_y = row * (enemy_height + enemy_gap) + 20
            enemy_list.append([enemy_x, enemy_y])

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

# Function to draw the enemies
def draw_enemies():
    for enemy in enemy_list:
        enemy_x, enemy_y = enemy
        pygame.draw.rect(screen, enemy_color, (enemy_x, enemy_y, enemy_width, enemy_height))

# Function to move the player
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

# Function to fire the bullet
def fire_bullet():
    global bullet_fired, bullet_x, bullet_y
    if not bullet_fired:
        bullet_x = player_x + (player_width // 2) - (bullet_radius // 2)
        bullet_y = player_y - bullet_radius
        bullet_fired = True

# Function to move the bullet
def move_bullet():
    global bullet_fired, bullet_x, bullet_y
    if bullet_fired:
        bullet_y -= bullet_speed
        # Check for collision with enemies
        for enemy in enemy_list:
            enemy_x, enemy_y = enemy
            if (bullet_x > enemy_x and bullet_x < enemy_x + enemy_width) and (bullet_y > enemy_y and bullet_y < enemy_y + enemy_height):
                enemy_list.remove(enemy)
                bullet_fired = False
                break
        # Check if the bullet goes out of bounds
        if bullet_y <= 0:
            bullet_fired = False

# Main game loop
clock = pygame.time.Clock()
create_enemies()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)
    draw_player()
    draw_enemies()
    move_player()
    fire_bullet()
    move_bullet()
    pygame.draw.circle(screen, BLUE, (bullet_x, bullet_y), bullet_radius)
    
    # Check if the game is over
    if len(enemy_list) == 0:
        print("Congratulations! You won!")
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
```

This code sets up a basic Space Invaders game with a player and enemies that move down the screen. The player can move left and right, and fire bullets to destroy the enemies. When all enemies are destroyed, the game ends with a congratulatory message.