Creating a complex "Asteroids" game from scratch requires some understanding of game development concepts, including handling graphics, game loops, physics, and user input. Below is a simplified example using Python and the `pygame` library. This example won't include all the bells and whistles you'd expect in a fully-featured game but will give you a solid foundation to build upon.

First, make sure you have Python installed on your system, and then install `pygame` if you haven’t already:

```bash
pip install pygame
```

Now, let's create a basic "Asteroids" clone:

```python
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Display dimensions
width, height = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Asteroids')

clock = pygame.time.Clock()

# Ship properties
ship_speed = 10
ship_radius = 20
ship_pos = [width / 2, height / 2]
ship_angle = 0

# Asteroid properties
asteroid_size_range = range(20, 60, 10)
asteroid_speed = 2

# List to store asteroids
asteroids = []

# Game objects
running = True
keys = pygame.key.get_pressed()

def gameLoop():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship_angle -= 5
                elif event.key == pygame.K_RIGHT:
                    ship_angle += 5
                elif event.key == pygame.K_SPACE:
                    break

        # Clear the background
        screen.fill(BLACK)

        # Draw the ship
        pygame.draw.circle(screen, WHITE, (int(ship_pos[0]), int(ship_pos[1])), ship_radius)

        # Draw asteroids
        for asteroid in asteroids:
            x, y = asteroid[0], asteroid[1]
            size = random.choice(asteroid_size_range)
            angle = random.randint(0, 360)
            new_x = int(x + math.cos(math.radians(angle)) * size)
            new_y = int(y + math.sin(math.radians(angle)) * size)
            pygame.draw.circle(screen, RED, (new_x, new_y), size)

        # Check collisions
        for asteroid in asteroids:
            x, y = asteroid[0], asteroid[1]
            ship_radius_half = ship_radius / 2
            if math.sqrt((x - int(ship_pos[0])) ** 2 + (y - int(ship_pos[1])) ** 2) <= ship_radius_half:
                asteroids.remove(asteroid)

        # Move the ship and asteroids
        ship_pos[0] += ship_speed * math.cos(math.radians(ship_angle))
        ship_pos[1] += ship_speed * math.sin(math.radians(ship_angle))
        for asteroid in asteroids:
            x, y = asteroid[0], asteroid[1]
            x += asteroid_speed * math.cos(math.radians(random.randint(0, 360)))
            y += asteroid_speed * math.sin(math.radians(random.randint(0, 360)))

        # Check for collisions with the screen
        for asteroid in asteroids:
            x, y = asteroid[0], asteroid[1]
            if x < 0 or x >= width or y < 0 or y >= height:
                asteroids.remove(asteroid)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Game start function
def main():
    global running
    running = True

    while running:
        gameLoop()

if __name__ == "__main__":
    main()
```

This script initializes a basic "Asteroids" game where you control a ship using arrow keys to move left and right, and space to exit the game. Asteroids spawn randomly, move towards the edges of the screen or off the edges, and can be destroyed by colliding with them.

To expand this into a more complex game, you might consider:

- Differently sized and shaped asteroids
- Asteroids that split when hit
- Power-ups or bonus items
- Improved graphics and animations

To achieve these, you'd need to further develop your game logic, potentially adding classes for different game entities (ships, asteroids, power-ups), handling sprite animations, and more sophisticated collision detection. For those enhancements, I recommend studying more about game development with Python and `pygame`, and perhaps exploring object-oriented programming principles to structure your code better.