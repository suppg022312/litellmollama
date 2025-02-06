Here's a simple implementation of Space Invaders using Python and the Pygame library. This game includes the basic features of Space Invaders, such as player movement, alien shooting, scoring, and level progression.

```python
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
ALIAN_WIDTH = 50
ALIAN_HEIGHT = 30
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 50
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
SPEED = 5

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the player and alien
player_pos = [100, HEIGHT - PLAYER_HEIGHT * 2]
alien_pos = [[150 + i * (ALIAN_WIDTH + 10), 50 + j * (ALIAN_HEIGHT + 20)] for i in range(5) for j in range(3)]
alien_speed_x = [-1 if random.random() < 0.8 else 1 for _ in range(15)]

# Set up the bullets
bullets = []

# Set up the score and level
score = 0
level = 1

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT]:
        player_pos[0] += SPEED

    # Ensure the player stays within the screen boundaries
    if player_pos[0] < 0:
        player_pos[0] = 0
    elif player_pos[0] > WIDTH - PLAYER_WIDTH:
        player_pos[0] = WIDTH - PLAYER_WIDTH

    # Move aliens
    for i, alien in enumerate(alien_pos):
        alien_pos[i][0] += alien_speed_x[i]

        # If the alien hits an edge of the screen, reverse its direction
        if alien_pos[i][0] < 0:
            alien_speed_x[i] = -alien_speed_x[i]
        elif alien_pos[i][0] > WIDTH - ALIAN_WIDTH:
            alien_speed_x[i] = -alien_speed_x[i]

    # Check for collision with aliens
    for bullet in bullets[:]:
        for i, alien in enumerate(alien_pos):
            if (bullet[1] + BULLET_HEIGHT > alien[1]) and (bullet[1] < alien[1] + ALIAN_HEIGHT) and (bullet[0] + BULLET_WIDTH > alien[0]) and (bullet[0] < alien[0] + ALIAN_WIDTH):
                # Destroy the bullet
                bullets.remove(bullet)
                # Destroy the alien
                alien_pos.pop(i)

    for i, alien in enumerate(alien_pos):
        if (alien[1] + ALIAN_HEIGHT > player_pos[1]) and (alien[1] < player_pos[1] + PLAYER_HEIGHT) and (alien[0] + ALIAN_WIDTH > player_pos[0]) and (alien[0] < player_pos[0] + PLAYER_WIDTH):
            # Game over
            print("Game Over")
            pygame.quit()
            sys.exit()

    # Check for bullet hitting aliens
    for bullet in bullets[:]:
        if bullet[1] < 0:
            # Destroy the bullet
            bullets.remove(bullet)
        else:
            alien_pos = [[alien[0], 50 + j * (ALIAN_HEIGHT + 20)] for i, alien in enumerate(alien_pos) for j in range(3)]
            for j, alien in enumerate(alien_pos):
                if (bullet[1] > alien[1]) and (bullet[1] < alien[1] + ALIAN_HEIGHT) and (bullet[0] + BULLET_WIDTH > alien[0]) and (bullet[0] < alien[0] + ALIAN_WIDTH):
                    # Destroy the bullet
                    bullets.remove(bullet)
                    # Destroy the alien
                    alien_pos.pop(j)

    # Fire a bullet if space is pressed
    if keys[pygame.K_SPACE]:
        bullets.append([player_pos[0], player_pos[1]])

    # Level up
    if score % 100 == 0:
        level += 1

    # Draw everything
    win.fill(WHITE)
    pygame.draw.rect(win, RED, (player_pos[0], player_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))
    for alien in alien_pos:
        pygame.draw.rect(win, RED, (alien[0], alien[1], ALIAN_WIDTH, ALIAN_HEIGHT))
    for bullet in bullets:
        pygame.draw.rect(win, RED, (bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT))

    # Draw the score
    text = font.render(f"Score: {score}", True, (10, 10, 10))
    win.blit(text, (10, 10))

    # Level display
    text = font.render(f"Level: {level}", True, (10, 10, 10))
    win.blit(text, (WIDTH - 150, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

    # Increase score if no aliens are left on screen
    if len(alien_pos) == 0:
        score += level * 5

# Close the window when it's closed
pygame.quit()
```

This is a basic implementation and does not include some of the features that you might see in a full game, such as better graphics, multiple types of aliens with different behaviors, power-ups or shields for the player.