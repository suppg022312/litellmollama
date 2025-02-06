
Here is an example of how you could create a simple Space Invaders game in Python using the pygame library:
```
import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions and title
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Load the game images
background_image = pygame.image.load("background.jpg").convert()
invader_image = pygame.image.load("invader.png").convert()
player_image = pygame.image.load("player.png").convert()
bullet_image = pygame.image.load("bullet.png").convert()

# Set the background color
background_color = (0, 0, 0)

# Create a group for all the sprites
all_sprites = pygame.sprite.Group()

# Create a player sprite
player = Player(screen_width / 2, screen_height - 50, 50, 50)
all_sprites.add(player)

# Create a group for all the bullets
bullets = pygame.sprite.Group()

# Loop until the user clicks the close button
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-5)
            elif event.key == pygame.K_RIGHT:
                player.move(5)
            elif event.key == pygame.K_SPACE:
                bullets.add(Bullet(player.x, player.y))

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.fill(background_color)
    for bullet in bullets:
        bullet.draw()
    player.draw()
    pygame.display.flip()

# Clean up
pygame.quit()
```
This is just a basic example, and you would need to add more functionality such as the invaders moving across the screen, and the player shooting them with bullets. You could also add sound effects and other elements to make the game more engaging.