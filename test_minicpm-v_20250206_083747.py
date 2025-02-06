Certainly! Here is an implementation of the classic Space Invaders game using Python:
```
import pygame
# Initialize Pygame libraries.
pygame.init()
# Set up display settings for the windowed mode. You can adjust these parameters to fit your screen size and desired resolution.
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
# Load graphics assets.
ship_image = pygame.image.load("assets/ship.png").convert_alpha()
enemy_images = [pygame.image.load("assets/enemy1.png"),
                pygame.image.load("assets/enemy2.png"),
                pygame.image.load("assets/enemy3.png")]
# Define the dimensions of each enemy and their health. You can modify these values to adjust difficulty.
enemy_width = 80
enemy_height = 54
enemy_health = [1, 2, 2]
# Initialize game state variables.
ship_speed = 7
bullet_speed = 30 * ship_speed # Increase bullet speed relative to player's movement speed
bullet_range = (screen_height - enemy_height) // int(enemy_height / bullet_speed)
bullet_damage = 5
score = 0

def draw_screen():
    screen.fill((24, 180, 159)) # Black background with greenish-blue gradient.
```
This code is just a starting point. You'll need to implement the rest of the game logic such as enemy movement and collision detection in order for it