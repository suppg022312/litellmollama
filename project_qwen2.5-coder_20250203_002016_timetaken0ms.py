Creating a Space Invaders game in Python can be a fun and educational project. We'll use the `pygame` library, which is a set of Python modules designed for writing video games. If you haven't installed `pygame`, you can do so using pip:

```bash
pip install pygame
```

Below is a simple implementation of Space Invaders in Python using `pygame`.

```python
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT // 3)]
enemy_list = [enemy_pos]
enemy_speed = 5

# Bullet settings
bullet_size = 10
bullet_pos = []
bullet_speed = 20

# Game clock
clock = pygame.time.Clock()

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, GREEN, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, bullet_pos):
    for enemy_pos in enemy_list:
        x_offset = 0
        y_offset = 0
        if (bullet_pos[0] >= enemy_pos[0] and bullet_pos[0] < (enemy_pos[0] + enemy_size)) or \
           (enemy_pos[0] >= bullet_pos[0] and enemy_pos[0] < (bullet_pos[0] + bullet_size)):
            if (bullet_pos[1] >= enemy_pos[1] and bullet_pos[1] < (enemy_pos[1] + enemy_size)) or \
               (enemy_pos[1] >= bullet_pos[1] and enemy_pos[1] < (bullet_pos[1] + bullet_size)):
                return True
    return False

def game_over(score):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over! Your score is: " + str(score), True, RED)
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()

# Main game loop
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT and x > 0:
                x -= player_speed
            elif event.key == pygame.K_RIGHT and x < WIDTH - player_size:
                x += player_speed
            elif event.key == pygame.K_SPACE:
                bullet_pos.append([x + player_size // 2, y])
    
    screen.fill(BLACK)
    
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    text = "Score:" + str(score)
    label = pygame.font.SysFont(None, 30).render(text, True, WHITE)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))
    
    if collision_check(enemy_list, bullet_pos):
        game_over(score)
    
    draw_enemies(enemy_list)
    
    for bullet in bullet_pos:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_size, bullet_size))
        bullet[1] -= bullet_speed
    
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    
    clock.tick(30)
    pygame.display.update()
```

### Explanation:
1. **Initialization**: We initialize `pygame` and set up the screen dimensions, colors, and other variables.
2. **Player Movement**: The player can move left or right using the arrow keys.
3. **Enemies**: Enemies are randomly generated at the top of the screen and move downwards.
4. **Bullets**: When the spacebar is pressed, a bullet is fired from the player's position.
5. **Collision Detection**: If an enemy collides with a bullet, it is removed from the list, and the score increases.
6. **Game Over**: The game ends when an enemy reaches the bottom of the screen.

This code provides a basic structure for a Space Invaders game. You can further enhance it by adding features like sound effects, more complex enemy behavior, and improved graphics.