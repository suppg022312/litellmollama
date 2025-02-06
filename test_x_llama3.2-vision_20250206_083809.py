Here's a simple implementation of the classic Space Invaders game using Python and the Pygame library.

**space_invaders.py**
```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_SIZE = 50
ENEMY_SIZE = 30
BULLET_SIZE = 10
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT - PLAYER_SIZE * 2, PLAYER_SIZE, PLAYER_SIZE)
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        elif keys[pygame.K_RIGHT]:
            self.speed_x = 5
        else:
            self.speed_x = 0
        if keys[pygame.K_UP]:
            self.speed_y = -5
        elif keys[pygame.K_DOWN]:
            self.speed_y = 5
        else:
            self.speed_y = 0
        self.x += self.speed_x
        self.y += self.speed_y

class Enemy(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.speed_x = 2
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        if self.x > WIDTH - ENEMY_SIZE or self.x < 0:
            self.speed_x *= -1
            self.y += ENEMY_SIZE

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_SIZE, BULLET_SIZE)
        self.speed_y = -10

    def move(self):
        self.y += self.speed_y

def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy(100, 100), Enemy(300, 200)]
    bullets = []
    score = 0
    font = pygame.font.SysFont("Arial", 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.centerx, player.top))

        screen.fill(BACKGROUND_COLOR)

        # Draw the player
        pygame.draw.rect(screen, (255, 0, 0), player)
        player.move()

        # Move and draw enemies
        for enemy in enemies:
            enemy.move()
            pygame.draw.rect(screen, (0, 255, 0), enemy)
            if enemy.colliderect(player):
                print("Game Over!")
                return

        # Draw bullets
        for bullet in bullets:
            bullet.move()
            pygame.draw.rect(screen, (0, 0, 255), bullet)
            if bullet.y < 0:
                bullets.remove(bullet)

        # Check collisions with enemies
        for enemy in enemies[:]:
            for bullet in bullets[:]:
                if bullet.colliderect(enemy):
                    score += 1
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        # Draw the score
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
```
This code creates a game window with a player that can move left and right using the arrow keys. The player shoots bullets by pressing the space bar, which collide with enemies to increase the score.

Note: This is a simplified version of Space Invaders, and there are many features that could be added to make it more like the original game (e.g., multiple levels, different types of enemies, power-ups).