Creating a full-fledged Space Invaders game in Python can be a fun and educational project. Below is a simple implementation using the `pygame` library, which is a popular choice for creating games in Python. Make sure you have `pygame` installed; you can do this by running `pip install pygame`.

First, let's set up the basic structure of the game:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_speed = 5
player_width = 10
player_height = 60
player_color = GREEN

# Invaders settings
invader_speed = 5
invader_width = 40
invader_height = 60
invader_color = BLUE

# Player position
player_x, player_y = WIDTH // 2, HEIGHT - 100

# Invaders list
invaders = []
num_rows = 3
num_cols = 8
invader_row = 0
invader_col = 4
spacing = 60

# Game settings
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)
score = 0
font_style = pygame.font.SysFont("bahnschrift", 25)
score_value = 0
game_over = False

# Load player image
player_image = pygame.image.load('spaceship.png')
player_image = pygame.transform.scale(player_image, (player_width, player_height))

def show_score(x, y):
    score = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(score, (x, y))

# Invaders generation function
def create_invaders():
    global invaders, invader_row, invader_col

    for row in range(num_rows):
        for col in range(num_cols):
            x = (col * (invader_width + spacing)) + 50
            y = (row * (invader_height + spacing)) + 100
            invaders.append([x, y])

# Main game loop
def main():
    global score, game_over

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= player_speed
                elif event.key == pygame.K_RIGHT:
                    player_x += player_speed

        # Clear screen
        screen.fill(BLACK)

        # Draw player
        screen.blit(player_image, (player_x, player_y))

        # Draw invaders
        for invader in invaders:
            pygame.draw.rect(screen, RED, (invader[0], invader[1], invader_width, invader_height))

        # Update score
        show_score(8, 50)

        # Game logic
        if player_x < 0:
            player_x = 0
        elif player_x > WIDTH - player_width:
            player_x = WIDTH - player_width

        # Move invaders
        for invader in invaders:
            y = invader[1]
            if y >= HEIGHT - invader_height:
                game_over = True
            if invader[1] < player_y and not game_over:
                invader[1] += 3
            elif invader[1] > player_y and not game_over:
                invader[1] -= 3

            # Check for collision with player
            if (player_x <= invader[0] + invader_width and
                player_x + player_width >= invader[0] and
                player_y <= invader[1] + invader_height and
                player_y + player_height >= invader[1]):
                game_over = True

            # Remove off-screen invaders
            if invader[1] > HEIGHT - invader_height:
                invaders.remove(invader)

        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Create invaders
create_invaders()

main()
```

**Additional Features to Consider:**

1. **Bullets and Enemy Shooting:** Allow the player to shoot bullets at the invaders, which can be a fun addition. You can use another image for the bullet and set up a timer to periodically create enemy shots that move towards the player.

2. **Score and Lives:** Implement a scoring system and allow players to have a limited number of lives, which can be deducted when hit by enemy fire or invaders.

3. **Power-Ups:** Introduce power-ups like shields or speed boosts that can temporarily enhance the player's abilities.

4. **Level System:** Create different levels with increasing difficulty and introduce new types of enemies.

5. **Sound Effects and Music:** Add sound effects for shooting, collisions, and background music to enhance the game's atmosphere.

Remember that this is a basic example, and you can expand it by adding more features and improving the graphics as needed. Have fun coding!