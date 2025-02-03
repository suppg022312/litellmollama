Creating a full-fledged Space Invaders game in Python can be quite extensive, but I'll provide you with a simplified version using the Pygame library. Pygame is a set of Python modules designed for writing video games.

First, ensure you have Pygame installed:

```sh
pip install pygame
```

Now, let's create a basic Space Invaders game. We'll break it down into smaller parts and use tools where necessary.

1. **Initialize Pygame and Set Up the Display**
2. **Create Game Objects (Player, Enemies, Bullets)**
3. **Handle User Input**
4. **Game Logic and Collision Detection**
5. **Main Game Loop**

Here's a step-by-step implementation:

### Step 1: Initialize Pygame and Set Up the Display

```python
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')  # Replace with your own icon
pygame.display.set_icon(icon)
```

### Step 2: Create Game Objects (Player, Enemies, Bullets)

```python
# Load images
player_img = pygame.image.load('player.png')  # Replace with your own player image
enemy_img = pygame.image.load('enemy.png')    # Replace with your own enemy image
bullet_img = pygame.image.load('bullet.png')  # Replace with your own bullet image

# Player settings
player_x = screen_width // 2 - 32
player_y = screen_height - 80
player_change_x = 0

# Enemy settings
enemy_x = []
enemy_y = []
enemy_change_x = 0.5
enemy_change_y = 40
num_enemies = 6

for i in range(num_enemies):
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(30, 150))

# Bullet settings
bullet_x = player_x
bullet_y = player_y
bullet_change_y = -3
bullet_state = "ready"  # "ready" - can't see bullet on the screen, "fire" - bullet is currently moving

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img, (x[i], y[i]))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))
```

### Step 3: Handle User Input

```python
# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -1
            if event.key == pygame.K_RIGHT:
                player_change_x = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # Key released check
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0

    # Update player position
    player_x += player_change_x

    # Keep the player within the screen boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64

    # Player on-screen drawing
    player(player_x, player_y)

    # Enemy movement and drawing
    for i in range(num_enemies):
        enemy_x[i] += enemy_change_x

        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            enemy_change_x *= -1
            enemy_y[i] += enemy_change_y

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement and drawing
    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = player_y
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y += bullet_change_y

    # Update the display
    pygame.display.update()
```

### Step 4: Game Logic and Collision Detection

```python
# Collision detection function
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(bullet_x - enemy_x, 2)) + (math.pow(bullet_y - enemy_y, 2)))
    if distance < 27:
        return True
    else:
        return False
```

### Step 5: Main Game Loop

```python
# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -1
            if event.key == pygame.K_RIGHT:
                player_change_x = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # Key released check
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0

    # Update player position
    player_x += player_change_x

    # Keep the player within the screen boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64

    # Player on-screen drawing
    player(player_x, player_y)

    # Enemy movement and drawing
    for i in range(num_enemies):
        enemy_x[i] += enemy_change_x

        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            enemy_change_x *= -1
            enemy_y[i] += enemy_change_y

        enemy(enemy_x[i], enemy_y[i], i)

        # Collision with player
        collision = is_collision(player_x, player_y, enemy_x[i], enemy_y[i])
        if collision:
            running = False

    # Bullet movement and drawing
    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = player_y
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y += bullet_change_y

    # Collision with enemy
    for i in range(num_enemies):
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, screen_width - 64)
            enemy_y[i] = random.randint(30, 150)

    # Update the display
    pygame.display.update()
```

### Step-by-Step Explanation

1. **Initialize Pygame and Set Up the Display**:
   - Initialize Pygame.
   - Define screen dimensions and create a screen object.
   - Set the game window title and icon.

2. **Create Game Objects (Player, Enemies, Bullets)**:
   - Load images for the player, enemies, and bullets.
   - Define initial positions and movement speeds for the player, enemies, and bullets.
   - Create functions to draw the player, enemies, and bullets on the screen.

3. **Handle User Input**:
   - Handle key events (left, right, space) to control the player's movement and shooting bullets.

4. **Game Logic and Collision Detection**:
   - Define a function to detect collisions between bullets and enemies.
   - Update enemy positions to move back and forth and change direction when hitting boundaries.
   - Update bullet positions and reset them after they go off-screen.

5. **Main Game Loop**:
   - Handle events, update game objects, check for collisions, and redraw the screen.

This is a simplified version of Space Invaders. You can expand it by adding more features such as sound effects, scoring system, levels, etc.