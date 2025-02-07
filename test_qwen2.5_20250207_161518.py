Creating a simple Space Invaders-style game in Python can be a fun project using the `pygame` library. Pygame is an excellent choice for beginners because it provides easy-to-use functions for graphics and sound.

First, you'll need to install pygame if you haven't already:

```bash
pip install pygame
```

Next, let's create a basic version of Space Invaders. The game will include the player spaceship that can move left and right, shooting bullets at aliens that move down from above. The aliens won't shoot back in this simple implementation.

Here is a step-by-step guide to creating a basic Space Invaders game:

1. **Initialize pygame**: Set up the screen and clock.
2. **Create assets**: Load images for the player, aliens, and bullets.
3. **Set up game objects**: Define classes for Player, Bullet, and Alien.
4. **Main loop**: Handle events, update game state, and render graphics.

Below is a complete example of how you might set this up:

```python
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_img = pygame.image.load('player.png')
alien_img = pygame.image.load('alien.png')
bullet_img = pygame.image.load('bullet.png')

# Player settings
player_speed = 10

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-60))
    
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += player_speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = alien_img
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self):
        self.rect.y += 1
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

# Create sprite groups
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()

# Player instance
player = Player()
player_group.add(player)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullet_group) < 10:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullet_group.add(bullet)
    
    # Update game objects
    keys = pygame.key.get_pressed()
    player.update(keys)
    
    for bullet in bullet_group:
        bullet.update()
    
    alien = Alien(SCREEN_WIDTH/2, 50)  # Example alien creation
    alien_group.add(alien)
    for alien in alien_group:
        alien.update()

    # Collisions between bullets and aliens
    hits = pygame.sprite.groupcollide(bullet_group, alien_group, True, True)

    # Draw everything
    screen.fill(BLACK)
    
    player_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
```

### Notes:
- **Images**: You need to provide `player.png`, `alien.png`, and `bullet.png`. These should be simple images of the player, an alien, and a bullet.
- **Aliens**: The game creates one alien at a time for demonstration. In a full version, you would create multiple aliens and handle their movement in a more complex pattern.

This is a very basic implementation to get you started with Space Invaders using Python and pygame. You can expand on this by adding features like health bars, power-ups, scoring systems, or even AI-controlled enemies.