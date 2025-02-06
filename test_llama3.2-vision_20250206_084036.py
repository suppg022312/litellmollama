Here's a simple implementation of the classic Space Invaders game using Python and the Pygame library. The game includes basic features such as player movement, alien invasion, and scoring.

**space_invaders.py**
```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the player
player_size = 50
player_x = WIDTH / 2 - player_size / 2
player_y = HEIGHT - 100

# Set up the aliens
alien_size = 30
aliens = []
for i in range(10):
    x = random.randint(0, WIDTH - alien_size)
    y = random.randint(0, HEIGHT / 4)
    aliens.append((x, y))

# Set up the bullets
bullets = []

# Set up the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append((player_x + player_size / 2, player_y))
            elif event.key == pygame.K_UP:
                player_y -= 10
            elif event.key == pygame.K_DOWN:
                player_y += 10

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Keep the player within bounds
    player_x = max(0, min(player_x, WIDTH - player_size))

    # Move the aliens
    for i, (x, y) in enumerate(aliens):
        x -= 2
        if x < 0:
            x = 800
            y += alien_size
        aliens[i] = (x, y)

    # Check for collisions with bullets
    for i, (x, y) in enumerate(aliens):
        for j, (bx, by) in enumerate(bullets):
            if (x < bx + 10 and x + alien_size > bx and
                    y < by + 20 and y + alien_size > by):
                del bullets[j]
                del aliens[i]
                score += 1

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    for x, y in aliens:
        pygame.draw.ellipse(screen, RED, (x, y, alien_size, alien_size))
    for bx, by in bullets:
        pygame.draw.rect(screen, WHITE, (bx, by, 10, 20))

    # Draw the score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame when the game window is closed
pygame.quit()
```
This code creates a window with a player ship at the bottom that can be moved left and right using the arrow keys. The goal of the game is to shoot down the incoming aliens (red circles) by pressing the space bar. Each alien shot will increase the score.

You'll need to have Pygame installed (`pip install pygame`) to run this code. Simply save it as `space_invaders.py` and run it with Python 3.x.

**Note:** This is a very basic implementation of Space Invaders, and there are many ways you could improve it (e.g., add more levels, power-ups, smoother graphics). If you're interested in learning more about game development or want to create your own games, I'd be happy to provide further guidance!