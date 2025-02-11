# Model Response: maryasov/yi-coder-cline
Generated on: 2025-02-11 01:56:23


<style>
.copy-button {
    position: absolute;
    top: 5px;
    right: 5px;
    padding: 5px 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    z-index: 1;
}
.code-container {
    position: relative;
    margin: 10px 0;
}
.copy-button:hover {
    background-color: #45a049;
}
.copy-button:active {
    background-color: #3d8b40;
}
</style>

<script>
function copyCode(buttonElement) {
    const codeBlock = buttonElement.parentElement.querySelector('code');
    const range = document.createRange();
    range.selectNode(codeBlock);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    try {
        document.execCommand('copy');
        buttonElement.textContent = 'Copied!';
        setTimeout(() => {
            buttonElement.textContent = 'Copy';
        }, 2000);
    } catch(e) {
        console.error('Failed to copy text:', e);
        buttonElement.textContent = 'Failed to copy';
    }
    window.getSelection().removeAllRanges();
}
</script>


## Original Task
<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```
create me a python based asteroid game 

```
</div>

## Model Solution
: Here is an example of how you can create a simple Asteroid game using Python and Pygame. This code will not run here as it requires a local environment to be set up, but you should be able to copy the code into your own IDE or text editor and run it there.

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
import pygame
import random 
from sys import exit  # To quit game   
pygame.init()    # Initialize all imported pygame modules 
screen = pygame.display.set_mode((800,600)) # Set the window resolution to (800,600)
clock = pygame.time.Clock()  # To control the game's speed   

class Player(pygame.sprite.Sprite): 
    def __init__(self):     
        super(Player, self).__init__()      
        img = pygame.image.load('player.png') # Load player image  
        self.image = pygame.transform.scale(img, (50, 50))   # Scale the image to 50x50 pixels    
        self.rect = self.image.get_rect()     
        self.mask = pygame.mask.from_surface(self.image)  # To detect collision between sprites      
        self.movement = [0, 0]   # Player movement speed       
                    
    def move(self):         
        keys = pygame.key.get_pressed()          
        if keys[pygame.K_UP]: self.movement[1] -= 5  # If up key pressed then decrease y-coordinate      
        elif keys[pygame.K_DOWN]: self.movement[1] += 5 # If down key pressed increase y-coordinate       
        if keys[pygame.K_LEFT]: self.movement[0] -= 5  # If left key pressed decrease x-coordinate      
        elif keys[pygame.K_RIGHT]: self.movement[0] += 5 # If right key pressed increase x-coordinate       
                    
class Asteroid(pygame.sprite.Sprite):   
    def __init__(self, pos):     
        super(Asteroid, self).__init__()      
        img = pygame.image.load('asteroid.png') # Load asteroid image  
        self.image = pygame.transform.scale(img, (50, 50))   # Scale the image to 50x50 pixels    
        self.rect = self.image.get_rect()      
        self.mask = pygame.mask.from_surface(self.image)  # To detect collision between sprites       
        self.pos = pos         
                   
def main(): 
    player = Player()     
    asteroids = pygame.sprite.Group() # Group of asteroids      
    while True:           
        clock.tick(60)  # Set game speed to 60 frames per second       
        for event in pygame.event.get():          
            if event.type == pygame.QUIT: exit()   # If player quits the game      
                    
        player.move() # Move the player     
        asteroids = group_collide(asteroids, player)  # Check for collision between asteroids and player       
        screen.fill((0, 0, 0)) # Fill screen with black color to clear previous frame      
        draw(player)   # Draw the player on the screen     
        draw(asteroids)    # Draw all asteroids on the screen  
        pygame.display.update() # Update display       
                            
def draw(sprite): 
    screen.blit(sprite.image, sprite.rect)   # Draw a sprite image to its position      
                         
def group_collide(group, player):  # Check for collision between a group of sprites and another sprite       
    for asteroid in (pygame.sprite.Group()) : # Create an empty group     
        if pygame.sprite.collide_mask(asteroid, player):   # If there is a collision      
            group.remove(asteroid)  # Remove the collided sprite from its group       
    return group 
                         
main() # Start game 
```
</div>

## Complete Code Summary
This section contains all the necessary code combined into a single, copyable block:

<div class="code-container">
<button class="copy-button" onclick="copyCode(this)">Copy</button>
```python
# Complete implementation
# Generated by: maryasov/yi-coder-cline
# Timestamp: 2025-02-11 01:56:23

import pygame
import random 
from sys import exit  # To quit game   
pygame.init()    # Initialize all imported pygame modules 
screen = pygame.display.set_mode((800,600)) # Set the window resolution to (800,600)
clock = pygame.time.Clock()  # To control the game's speed   

class Player(pygame.sprite.Sprite): 
    def __init__(self):     
        super(Player, self).__init__()      
        img = pygame.image.load('player.png') # Load player image  
        self.image = pygame.transform.scale(img, (50, 50))   # Scale the image to 50x50 pixels    
        self.rect = self.image.get_rect()     
        self.mask = pygame.mask.from_surface(self.image)  # To detect collision between sprites      
        self.movement = [0, 0]   # Player movement speed       
                    
    def move(self):         
        keys = pygame.key.get_pressed()          
        if keys[pygame.K_UP]: self.movement[1] -= 5  # If up key pressed then decrease y-coordinate      
        elif keys[pygame.K_DOWN]: self.movement[1] += 5 # If down key pressed increase y-coordinate       
        if keys[pygame.K_LEFT]: self.movement[0] -= 5  # If left key pressed decrease x-coordinate      
        elif keys[pygame.K_RIGHT]: self.movement[0] += 5 # If right key pressed increase x-coordinate       
                    
class Asteroid(pygame.sprite.Sprite):   
    def __init__(self, pos):     
        super(Asteroid, self).__init__()      
        img = pygame.image.load('asteroid.png') # Load asteroid image  
        self.image = pygame.transform.scale(img, (50, 50))   # Scale the image to 50x50 pixels    
        self.rect = self.image.get_rect()      
        self.mask = pygame.mask.from_surface(self.image)  # To detect collision between sprites       
        self.pos = pos         
                   
def main(): 
    player = Player()     
    asteroids = pygame.sprite.Group() # Group of asteroids      
    while True:           
        clock.tick(60)  # Set game speed to 60 frames per second       
        for event in pygame.event.get():          
            if event.type == pygame.QUIT: exit()   # If player quits the game      
                    
        player.move() # Move the player     
        asteroids = group_collide(asteroids, player)  # Check for collision between asteroids and player       
        screen.fill((0, 0, 0)) # Fill screen with black color to clear previous frame      
        draw(player)   # Draw the player on the screen     
        draw(asteroids)    # Draw all asteroids on the screen  
        pygame.display.update() # Update display       
                            
def draw(sprite): 
    screen.blit(sprite.image, sprite.rect)   # Draw a sprite image to its position      
                         
def group_collide(group, player):  # Check for collision between a group of sprites and another sprite       
    for asteroid in (pygame.sprite.Group()) : # Create an empty group     
        if pygame.sprite.collide_mask(asteroid, player):   # If there is a collision      
            group.remove(asteroid)  # Remove the collided sprite from its group       
    return group 
                         
main() # Start game 

```
</div>

## Usage Instructions
1. The code snippets above are wrapped in markdown code blocks with copy buttons
2. You can copy any code block by clicking the "Copy" button
3. The complete implementation is available in the "Complete Code Summary" section
4. Make sure to follow any setup instructions provided in the response

## Metadata
- Model: maryasov/yi-coder-cline
- Timestamp: 2025-02-11 01:56:23
- File: test_maryasov_yi-coder-cline_20250211_015623.md
