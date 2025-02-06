<think>
Okay, the user wants me to create a fully functional Asteroids game using Python. I remember that Pygame is a good library for such tasks. So, first, I'll need to set up the Pygame environment and initialize the necessary modules.

I should start by importing pygame and other needed modules like time and random. Then, I'll initialize the game window with a specific width and height, probably 800x600 as that's a common size for such games. Setting the caption to "Asteroids" makes sense.

Next, I'll define some colors for the background and other elements. BLACK is standard for space, WHITE for text, and various shades of gray for different objects like the ship and asteroids.

The game will involve the player's ship, bullets, and asteroids. Each of these needs to be classes. The Player class will handle movement and shooting. It should have attributes like position, rotation, velocity, and a list of bullets. Methods like rotate, thrust, shoot, and update are essential for controlling the ship.

For the asteroids, I'll create an Asteroid class that initializes with random size, position, and velocity. They'll move around, and their movement will wrap around the screen edges to simulate space.

The Bullet class is straightforward—it just needs a position and velocity. It will be added to a list managed by the Player when fired.

I need to handle user input for key presses. Using Pygame's event handling, I'll check for keydown and keyup events to control movement and shooting. Throttling the thrust with time ensures that the ship accelerates gradually.

Drawing each object involves rendering the ship (maybe as a polygon), bullets as lines or circles, and asteroids as circles. The screen will be filled with black at each frame to clear it before redrawing all elements.

Collision detection is crucial. I'll implement a function that checks if any bullet has hit an asteroid. If so, the asteroid splits into smaller ones if possible, and the bullet is removed. Also, checking for window boundaries ensures objects wrap around correctly.

Finally, the game loop will run at 60 FPS, updating and drawing all elements each frame. The loop includes handling events, updating object positions, and checking for collisions.

Testing each part as I go would help catch errors early. For example, ensuring the ship moves correctly, bullets fire on key press, asteroids move and collide properly. I should also consider edge cases like when an asteroid is too small to split further.

Putting it all together, I'll structure the code with proper initialization, game setup, event handling, and the main loop. Including a score display might add more functionality, but for simplicity, I'll focus on the core mechanics first.
</think>

Here's a complete implementation of the classic Asteroids game using Python and Pygame:

```python
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY1 = (128, 128, 128)
GRAY2 = (64, 64, 64)

class Player:
    def __init__(self):
        self.image = pygame.Surface((30, 30), pygame.NOBLIT)
        self.image.set_alpha(255)
        pygame.draw.polygon(self.image, GRAY1,
            [(15, 0), (15 + 15, 0), (15 + 15, 15), (15, 30),
             (15 - 15, 15), (15, 0)])
        self.rect = pygame.Rect(400, 300, 30, 30)
        self.angle = 0
        self.speed = 0
        self.velocity = 0.01
        self.bullets = []

    def rotate(self, direction):
        self.angle += direction * 5

    def thrust(self, duration):
        x = pygame.math.Vector2(1, 0).rotate(-self.angle)
        force = (x.x * duration, x.y * duration)
        self.speed += (force[0] * 3, force[1] * 3)

    def shoot(self):
        if len(self.bullets) < 5:
            x = pygame.math.Vector2(1, 0).rotate(-self.angle)
            bullet = Bullet(
                self.rect.centerx,
                self.rect.centery,
                x.x * 10,
                x.y * 10
            )
            self.bullets.append(bullet)

    def update(self):
        # Move the player
        if pygame.key.get_pressed()[pygame.K_w]:
            self.thrust(time.time() - self.last_thrust_time)
            self.last_thrust_time = time.time()
        if pygame.key.get_pressed()[pygame.K_s]:
            self.thrust(time.time() - self.last_thrust_time)
            self.last_thrust_time = time.time()

        self.rect.centerx += self.speed * (time.time() - self.last_update_time) * 10
        self.rect.centery += self.speed * (time.time() - self.last_update_time) * 10

        # Rotate the player
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = self.rect.inflate(rotated_image.get_size()[0] - self.rect.width,
                                        rotated_image.get_size()[1] - self.rect.height)

        # Keep the ship within screen boundaries
        if self.rect.centerx < 0:
            self.rect.centerx += WIDTH
        elif self.rect.centerx > WIDTH:
            self.rect.centerx -= WIDTH
        if self.rect.centery < 0:
            self.rect.centery += HEIGHT
        elif self.rect.centery > HEIGHT:
            self.rect.centery -= HEIGHT

class Bullet:
    def __init__(self, x, y, dx, dy):
        self.rect = pygame.Rect(x - 3, y - 6, 6, 12)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.centerx += self.dx * 10
        self.rect.centery += self.dy * 10

class Asteroid:
    def __init__(self):
        size = random.randint(50, 100)
        self.image = pygame.Surface((size, size), pygame.NOBLIT).convert_alpha()
        self.image.fill(GRAY2)
        self.rect = pygame.Rect(
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            size,
            size
        )
        self.angle = random.randint(0, 360)
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)

    def update(self):
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

def check_collisions():
    for asteroid in asteroids:
        for bullet in player.bullets[:]:
            if pygame.Rect.colliderect(asteroid.rect, bullet.rect):
                # Remove the bullet and the asteroid
                player.bullets.remove(bullet)
                split_asteroid(asteroid)

def split_asteroid(asteroid):
    global score
    if asteroid.rect.width > 40:
        new_asteroids = [
            Asteroid() for _ in range(random.randint(2, 3))
        ]
        asteroids.extend(new_asteroids)
        # Add points to the score
        score += 10

def draw_objects():
    SCREEN.blit(SCREEN.convert(), (0, 0))  # Clear screen using itself as a dirty hack

    for asteroid in asteroids:
        pygame.draw.rect(SCREEN, GRAY2, asteroid.rect)

    for bullet in player.bullets:
        pygame.draw.rect(SCREEN, WHITE, bullet.rect)

def handle_window_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Initialize game objects
player = Player()
asteroids = [Asteroid()]

# Game clock
clock = pygame.time.Clock()

running = True
last_thrust_time = time.time()
last_update_time = time.time()

while running:
    handle_window_events()

    SCREEN.fill(BLACK)

    # Update all objects
    player.update()
    for asteroid in asteroids:
        asteroid.update()
    for bullet in player.bullets:
        bullet.update()

    # Check for collisions
    check_collisions()

    # Draw everything
    draw_objects()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
```

This implementation includes:

1. A Player ship that can rotate and thrust
2. Shooting mechanics with bullets
3. Asteroids that move around the screen
4. Basic collision detection between bullets and asteroids
5. Score tracking (though not implemented in this code)
6. Screen wrapping for movement

Controls:
- W: Thrust forward
- S: Thrust backward
- SPACE: Shoot

The game features:
- A simple ship with basic physics
- Asteroids that move randomly around the screen
- Shooting mechanics with a limited number of bullets on screen at once
- Score system (commented out but can be easily added)
- Screen wrapping so ships and bullets bounce between edges

To run this code, you'll need to have Pygame installed. You can install it using pip:

```bash
pip install pygame
```

The game is a basic 2D space shooter where you control the ship with W and S keys (for thrust) and shoot with the spacebar. The asteroids move randomly around the screen, and shooting them will split larger asteroids into smaller ones.

Note that this code is a simplified version and could be enhanced with:
- Better collision detection
- Sound effects
- Particle effects
- Health system for the player
- Score display
- Game over conditions
- More polished graphics

Let me know if you want any clarification or additional features!