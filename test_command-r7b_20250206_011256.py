Creating an entire asteroid-themed video game from scratch in Python can be quite complex, but I can provide you with a simplified version to get you started. This version will be a basic command-line game using the `pygame` library for graphics and input handling. If you don't have `pygame` installed, you can install it using `pip install pygame`.

Here's a simple implementation:

1. **Install Pygame**: If you haven't already, install Pygame using pip:
   ```sh
   pip install pygame
   ```

2. **Python Code for the Game**:

```python
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Display settings
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
SHIP_SIZE = 10
SHIP_COLOR = GREEN
SHIP_POSITION = [WIDTH // 2, HEIGHT - 50]

# Asteroid settings
ASTEROID_SIZE = [20, 20]
ASTEROID_COLORS = [(100, 149, 237), (238, 130, 238), (236, 154, 99)]  # Colors for asteroids

# Bullet settings
BULLET_SIZE = 5
BULLET_COLOR = BLUE
BULLET_SPEED = 10

# Game settings
LIVES = 3
SCORE = 0

def draw_ship(x, y):
    pygame.draw.rect(screen, SHIP_COLOR, (x - SHIP_SIZE // 2, y - SHIP_SIZE // 2, SHIP_SIZE, SHIP_SIZE))

def draw_asteroid():
    color = random.choice(ASTEROID_COLORS)
    pygame.draw.rect(screen, color, (random.randrange(0, WIDTH - ASTEROID_SIZE[0]), 
                                      random.randrange(0, HEIGHT - ASTEROID_SIZE[1]), 
                                      ASTEROID_SIZE[0], ASTEROID_SIZE[1]))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, BULLET_COLOR, (bullet[0], bullet[1]), BULLET_SIZE)

def check_collisions():
    global LIVES, SCORE

    # Player-asteroid collision
    for asteroid in asteroids:
        if asteroid[0] < SHIP_POSITION[0] + SHIP_SIZE // 2 and \
           asteroid[0] + ASTEROID_SIZE[0] > SHIP_POSITION[0] and \
           asteroid[1] < SHIP_POSITION[1] + SHIP_SIZE // 2 and \
           asteroid[1] + ASTEROID_SIZE[1] > SHIP_POSITION[1]:
            lives -= 1
            asteroids.remove(asteroid)

    # Player-bullet collision
    for bullet in bullets:
        for asteroid in asteroids[:]:
            if asteroid[0] < bullet[0] + BULLET_SIZE // 2 and \
               asteroid[0] + ASTEROID_SIZE[0] > bullet[0] and \
               asteroid[1] < bullet[1] + BULLET_SIZE // 2 and \
               asteroid[1] + ASTEROID_SIZE[1] > bullet[1]:
                asteroids.remove(asteroid)
                SCORE += 50

    # Check for game over
    if lives <= 0:
        pygame.quit()
        quit()

# Game loop
clock = pygame.time.Clock()
lives, score = LIVES, SCORE
bullets = []
asteroids = []
running = True
ship_direction = [0, 0]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not ship_direction[0]:
                ship_direction[0] = -1
            elif event.key == pygame.K_RIGHT and not ship_direction[0]:
                ship_direction[0] = 1
            elif event.key == pygame.K_UP and not ship_direction[1]:
                ship_direction[1] = -1
            elif event.key == pygame.K_DOWN and not ship_direction[1]:
                ship_direction[1] = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                ship_direction[0] = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                ship_direction[1] = 0

    # Move the player
    SHIP_POSITION[0] += ship_direction[0]
    SHIP_POSITION[1] += ship_direction[1]
    SHIP_POSITION[0] = max(0, min(SHIP_POSITION[0], WIDTH - SHIP_SIZE))
    SHIP_POSITION[1] = max(0, min(SHIP_POSITION[1], HEIGHT - SHIP_SIZE))

    # Generate new asteroids when the player is idle for a while
    if not ship_direction[0] and not ship_direction[1]:
        time.sleep(2)  # Simulate a short delay
        asteroids.append((random.randrange(0, WIDTH - ASTEROID_SIZE[0]),
                         random.randrange(0, HEIGHT - ASTEROID_SIZE[1])))

    # Move bullets
    bullets = [(x + BULLET_SPEED * ship_direction[0], y + BULLET_SPEED * ship_direction[1]) for x, y in bullets]
    bullets = [bullet for bullet in bullets if 0 <= bullet[0] < WIDTH and 0 <= bullet[1] < HEIGHT]

    # Clear screen
    screen.fill(BLACK)

    # Draw elements
    draw_ship(*SHIP_POSITION)
    for asteroid in asteroids:
        draw_asteroid()
    draw_bullets()

    # Update score display
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {SCORE} Lives: {lives}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
```

### Explanation:

1. **Initialization**: We initialize Pygame and set up the display with a specified width, height, and title.

2. **Functions**:
   - `draw_ship`: Draws the player's ship.
   - `draw_asteroid`: Randomly draws an asteroid on the screen.
   - `draw_bullets`: Draws all active bullets.
   - `check_collisions`: Checks for collisions between the player, asteroids, and bullets, and updates the game state accordingly.

3. **Game Loop**:
   - Handles input (arrow keys) to move the ship.
   - Generates new asteroids when the player is stationary for a short period.
   - Moves bullets based on ship direction.
   - Clears the screen and redraws all elements in each frame.
   - Updates the score and display lives.

4. **Collision Detection**: The `check_collisions` function checks for collisions and updates the game state, including lives and asteroids.

### Running the Game:
- Save the code to a file, e.g., `asteroids.py`.
- Run it with Python: `python asteroids.py`.

This is a basic implementation. You can expand upon it by adding more features like multiple levels, enemy ships, power-ups, and more advanced graphics and physics.