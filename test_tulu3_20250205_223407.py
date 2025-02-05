Creating an Asteroids game involves quite a bit of code, especially when integrating with Streamlit for web presentation. Below is a simplified version of how you might start building such a game using Python, Pygame (for handling graphics and game logic), and Streamlit (for creating the user interface).

### Step 1: Set up your environment

First, ensure you have the necessary packages installed:

```sh
pip install pygame streamlit
```

### Step 2: Write the Asteroids Game Code

**asteroids_game.py**

This file will contain the core game logic using Pygame.

```python
import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define some constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SHIP_SIZE = 20
ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE = 10, 50
MAX_ASTEROIDS = 10
SPEED_FACTOR = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Ship:
    def __init__(self):
        self.position = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = Vector(0, 0)

    def move(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # Keep ship on screen
        if self.position.x < SHIP_SIZE:
            self.position.x = SHIP_SIZE
        elif self.position.x > SCREEN_WIDTH - SHIP_SIZE:
            self.position.x = SCREEN_WIDTH - SHIP_SIZE
        if self.position.y < SHIP_SIZE:
            self.position.y = SHIP_SIZE
        elif self.position.y > SCREEN_HEIGHT - SHIP_SIZE:
            self.position.y = SCREEN_HEIGHT - SHIP_SIZE

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity.x = -SPEED_FACTOR
            elif event.key == pygame.K_RIGHT:
                self.velocity.x = SPEED_FACTOR
            elif event.key == pygame.K_UP:
                self.velocity.y = -SPEED_FACTOR
            elif event.key == pygame.K_DOWN:
                self.velocity.y = SPEED_FACTOR

class Asteroid:
    def __init__(self, pos):
        self.position = Vector(*pos)
        self.size = random.randint(ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE)
        self.velocity = Vector(random.random() * 2 - 1, random.random() * 2 - 1)

    def move(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # Off-screen wrap-around
        if self.position.x < -self.size:
            self.position.x = SCREEN_WIDTH + self.size
        elif self.position.x > SCREEN_WIDTH + self.size:
            self.position.x = -self.size
        if self.position.y < -self.size:
            self.position.y = SCREEN_HEIGHT + self.size
        elif self.position.y > SCREEN_HEIGHT + self.size:
            self.position.y = -self.size

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, [int(self.position.x), int(self.position.y)], self.size)

def main():
    # Initialize game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')

    ship = Ship()
    asteroids = [Asteroid((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))) for _ in range(MAX_ASTEROIDS)]

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            ship.handle_event(event)

        # Update game state
        screen.fill(BLACK)  # Clear the screen
        ship.move()

        # Asteroids movement and drawing
        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)

        # Drawing the ship
        pygame.draw.circle(screen, WHITE, [int(ship.position.x), int(ship.position.y)], SHIP_SIZE)

        # Update display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
```

### Step 3: Create a Streamlit Interface

**streamlit_asteroids.py**

```python
import streamlit as st
import webbrowser
from subprocess import Popen, CREATE_NO_WINDOW


def launch_game():
    # Open the game in a new browser tab.
    url = "http://localhost:8501"
    webbrowser.open(url, new=2)  # open in a new tab

# Start Streamlit application
st.title("Asteroids Game")

launch_button = st.button("Launch Asteroids Game")
if launch_button:
    game_process = Popen(["python", "asteroids_game.py"], creationflags=CREATE_NO_WINDOW)
```

### Step 4: Running the Application

1. **Run the Streamlit application**:

   ```sh
   streamlit run streamlit_asteroids.py
   ```

2. Open a browser and navigate to `http://localhost:8501` (or click on the "Launch Asteroids Game" button in your Streamlit app).

This is just a starting point. An actual Asteroids game would involve collision detection, scoring, and probably more complex asteroid spawning mechanics and player ships with better handling.

**Important Notes:**

- The code above includes minimalistic logic for an Asteroids game to keep it simple. For real-world applications, consider separating concerns (e.g., game logic in one module, user interface in another), using object-oriented programming principles more rigorously, handling edge cases, and improving the visual aspects of your game.
- Streamlit is great for prototyping or creating dashboards but might not be the best choice for performance-critical applications like games. You could consider alternatives such as Flask with HTML/CSS/JS, Pygame's built-in windowing, or dedicated JavaScript frameworks like Phaser if you plan to make a full-fledged game.
- Always ensure your development environment is correctly set up and test thoroughly before deploying your application.

This example gives you a basic framework to start expanding upon. Happy coding!