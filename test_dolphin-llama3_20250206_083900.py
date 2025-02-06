```python
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# Game variables
player_x = screen_width / 2
player_y = screen_height - 50
player_speed = 5

alien_x = 0
alien_y = 50
alien_speed = 3

# Score variable
score = 0

# Load images
player_image = pygame.image.load('player.png')
alien_image = pygame.image.load('alien.png')

# Game loop
running = True
while running:
    # Fill the background with black
    screen.fill((0, 0, 0))

    # Get all events (e.g., close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of the player and aliens
    player_x += player_speed
    alien_x += alien_speed

    # Draw everything
    screen.blit(player_image, (player_x, player_y))
    screen.blit(alien_image, (alien_x, alien_y))

pygame.quit()
```