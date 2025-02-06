Creating a fully functional Asteroids game in Python involves several components such as game logic, collision detection, scoring, handling user input, and more. Below is a simplified version of an Asteroids game using the `pygame` library. This example provides a basic structure, and you can expand it with more features like power-ups, different ship sizes, or enhanced graphics.

First, ensure you have `pygame` installed. You can install it via `pip`:

```sh
pip install pygame
```

Now, here's a basic implementation of an Asteroids game:

```python
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Ship variables
ship_speed = 5
ship_size = 20
ship_x = WIDTH // 2
ship_y = HEIGHT // 2

# Asteroid variables
asteroid_speed = 0.5
max_asteroid_size = 10
asteroid_list = []

clock = pygame.time.Clock()

def game_loop():
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Asteroids')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Draw the background (sky)
        pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, HEIGHT])

        # Handle ship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ship_y -= ship_speed
        if keys[pygame.K_DOWN]:
            ship_y += ship_speed

        # Draw the ship
        pygame.draw.rect(screen, GREEN, [ship_x, ship_y, ship_size, ship_size])

        # Check for collisions with the top and bottom borders
        if ship_y < 0:
            ship_y = 0
        if ship_y + ship_size >= HEIGHT:
            ship_y = HEIGHT - ship_size

        # Asteroid logic
        for asteroid in asteroid_list:
            x, y = asteroid[0], asteroid[1]
            if x + asteroid_size // 2 < 0 or x + asteroid_size // 2 >= WIDTH or y + asteroid_size // 2 < 0 or y + asteroid_size // 2 >= HEIGHT:
                # Out of bounds, remove the asteroid
                asteroid_list.remove(asteroid)
                continue

            # Move the asteroid
            x, y = int(x), int(y)
            x += asteroid_speed
            if x % 10 == 0:
                asteroid_list.append([x, y])  # Restart the asteroid in a random new position when it leaves the screen

            # Check for collision with the ship
            if abs(ship_x - x) <= ship_size and abs(ship_y - y) <= ship_size:
                print(f"Player hit an asteroid!")
                asteroid_list.remove(asteroid)
                # Change ship size or restart level, etc., here
                ship_size /= 2  # Example: Reduce ship size when hitting an asteroid
                if not ship_size:
                    print("Game Over")
                    running = False

        pygame.display.update()

        # Cap the framerate at 60 FPS
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
```

This script creates a very basic version of an Asteroids game where you control a ship with arrow keys to avoid asteroids and not crash into the borders of the screen. When you hit an asteroid, the ship's size decreases (you can implement resizing logic or game over conditions based on this).

To expand this, you could:

- Add more complex asteroid movement patterns.
- Implement different sized asteroids.
- Include power-ups that the player can collect.
- Use sounds and music to enhance the gaming experience.
- Improve collision detection for more realistic physics.

Remember, game development can be as simple or as complex as you want it to be. This example is a starting point to build upon.