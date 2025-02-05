Creating a full-fledged Asteroids-style game from scratch is quite complex and involves programming skills in languages like Python (with libraries such as Pygame), JavaScript with HTML5 canvas, or other game development frameworks. However, I can guide you through the basic steps to create a simple version of an asteroids game using Python and the Pygame library.

### Step 1: Install Pygame
First, make sure you have Python installed on your system. Then, install Pygame by running:
```bash
pip install pygame
```

### Step 2: Set Up Your Game Environment

Here's a basic setup for an asteroids game:

- **Game window**: Define the size of the window and initialize it.
- **Sprites**: Create classes for the spaceship, bullets (laser shots), and asteroids.
- **Movement and Collision Detection**: Implement functions to handle movement, shooting, collision detection, etc.

### Step 3: Game Loop

The game loop will continuously update the state of your game until the player quits. This includes moving objects around the screen, detecting collisions, updating scores, lives, and so on.

Here’s a simple structure for an asteroids game in Python using Pygame:

```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Asteroids Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA) # Transparent surface
        pygame.draw.polygon(self.image, WHITE, [(15,0),(29,30),(15,60),(1,30)])
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface((size * 20, size * 20), pygame.SRCALPHA)
        # Simplified asteroid drawing (you can use more sophisticated shapes and images here)
        pygame.draw.circle(self.image, WHITE, (int(size*10), int(size*10)), int(size*10))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH - 50) # Random start position
        self.rect.y = random.randint(-HEIGHT, -20)
        self.speed_y = random.randint(1,3)

    def update(self):
        self.rect.y += self.speed_y

# Main game loop
def main():
    clock = pygame.time.Clock()
    spaceship = Spaceship()
    all_sprites = pygame.sprite.Group(spaceship)
    asteroids = pygame.sprite.Group()

    for _ in range(5):  # Add initial asteroids
        asteroid = Asteroid(random.randint(1,3))
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    running = True

    while running:
        clock.tick(60)  # Frame rate (frames per second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Example of adding a laser shot on space bar press

        all_sprites.update()

        SCREEN.fill(BLACK)  # Background color

        all_sprites.draw(SCREEN)
        
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == '__main__':
    main()
```

### Step 4: Expand Your Game
To make your game more interesting, consider adding:
- Different types of asteroids with varying sizes and speeds.
- Shooting mechanics (lasers).
- Collision detection between spaceship and asteroids.
- Keeping score and lives.

This code is a basic starting point. You can expand it by adding features like sound effects, different levels, power-ups, and better graphics.

Would you like to learn more about any specific part of this game or need help with a particular feature?