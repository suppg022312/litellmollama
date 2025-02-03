 Creating a Space Invaders game involves several steps, including setting up the game environment, creating the game objects (aliens and player ship), handling user input, and managing game logic. Below is a simple implementation using Python and the Pygame library, which is commonly used for game development in Python.

First, make sure you have Pygame installed. You can install it using pip:

```sh
pip install pygame
```

Here's a basic implementation of a Space Invaders game:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_width, player_height = 50, 30
player_x = (width - player_width) / 2
player_y = height - player_height - 10
player_speed = 5

# Set up the alien
alien_width, alien_height = 30, 30
alien_x = (width - alien_width) / 2
alien_y = 50
alien_speed = 2

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (alien_x, alien_y, alien_width, alien_height))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
```

This code sets up a basic game window with a player and an alien. The player can move left and right using the arrow keys, and the alien remains stationary for now. The game updates every 60 frames per second.

To make the game more interesting, you can add more features like shooting bullets, increasing the difficulty, and more complex movement patterns for the aliens. Here's a more advanced version that includes bullets and scoring:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_width, player_height = 50, 30
player_x = (width - player_width) / 2
player_y = height - player_height - 10
player_speed = 5

# Set up the alien
alien_width, alien_height = 30, 30
alien_x = (width - alien_width) / 2
alien_y = 50
alien_speed = 2
alien_direction = 1
alien_drop_speed = 10

# Set up the bullet
bullet_width, bullet_height = 5, 15
bullet_x = player_x + player_width / 2 - bullet_width / 2
bullet_y = player_y - bullet_height
bullet_speed = 10
bullet_state = 'ready'

# Game loop
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_x = player_x + player_width / 2 - bullet_width / 2
                bullet_y = player_y - bullet_height
                bullet_state = 'fire'

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move the bullet
    if bullet_state == 'fire':
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = 'ready'

    # Move the alien
    alien_x += alien_direction * alien_speed
    if alien_x <= 0 or alien_x >= width - alien_width:
        alien_y += alien_drop_speed
        alien_direction *= -1

    # Check for collisions
    if bullet_y < alien_y + alien_height and bullet_y > alien_y and bullet_x + bullet_width > alien_x and bullet_x < alien_x + alien_width:
        bullet_state = 'ready'
        score += 1
        alien_x = (width - alien_width) / 2
        alien_y = 50

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (alien_x, alien_y, alien_width, alien_height))
    if bullet_state == 'fire':
        pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
```

This version includes a bullet that the player can shoot with the spacebar. The bullet moves upwards, and when it collides with an alien, it resets the alien's position and increases the score. The game also tracks the player's score.

You can further enhance this game by adding more features, such as different types of aliens with different behaviors, sound effects, and a game over state.