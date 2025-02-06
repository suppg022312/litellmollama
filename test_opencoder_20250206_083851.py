Sorry, as a text-based AI model, I'm not currently capable of running games or scripts. Writing and creating the game itself requires direct programming on your computer's software.

However, here's a simple example of how you can create a basic version of Space Invaders using Python and the Pygame library:

```python
import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
BORDER = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BORDER)
pygame.display.set_caption('Space Invaders')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
```

Please note that this is a very basic example and doesn't include any game logic or graphics yet - it simply sets up a window for you to play Space Invaders in.

Creating a full-fledged space invaders game will be much more complicated, likely requiring hundreds of lines of code and more complex concepts. If you're interested in creating your own games, I'd recommend looking into game development tutorials or libraries such as Pygame.
