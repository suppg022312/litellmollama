Certainly! Below is a simple implementation of a text-based Space Invaders game using Python. This version won't feature graphical elements but will simulate the essence of the game through text output. For a full graphical version, you would need to use libraries such as Pygame.

```python
import random

# Define the player's ship and invader's positions
player_position = [5, 15]
invaders_positions = [[random.randint(1, 20), random.randint(1, 20)] for _ in range(11)]

# Define game over condition: when invaders reach the top
game_over = False
player_dead = False

# Game loop
while not game_over:
    print("\n")
    
    # Move invaders down
    for invader in invaders_positions:
        if invader[1] > 20:  # If at the bottom of the screen
            invaders_positions.remove(invader)  # Remove it from the list
            print("You lost! Game over.")
            game_over = True
        else:
            invader[1] -= 1  # Move down

    # Print invaders and player
    for i, invader in enumerate(invaders_positions):
        print(f"Invader {i+1} at ({invader[0]}, {invader[1]})")
    print(f"Player at ({player_position[0]}, {player_position[1]})")

    # Move player
    if player_position[1] == 0:  # If player is at the bottom
        player_dead = True
        print("You died! Game over.")
        game_over = True
    else:
        # Randomly move up or down
        if random.randint(0, 1) == 0:
            player_position[1] -= 1
        else:
            player_position[1] += 1

    # Check if player shoots and hits an invader
    if player_position[0] == 5:  # Assuming player shoots horizontally at the center
        for i, invader in enumerate(invaders_positions):
            if invader[0] == 10:  # Assuming a hit when directly in front of the player
                invaders_positions.pop(i)  # Remove the hit invader
                print(f"Player shot Invader {i+1}!")
                game_over = True
                break

    # Check for game over
    if game_over:
        break

print("\nGame Over. Press Enter to play again.")
input("Press Enter to continue...")
```

This simple game simulates the movement of invaders from the top of the screen downwards, with the player-controlled ship able to move up and down and shoot horizontally. The game ends when either all invaders have reached the bottom or the player's ship has been hit.

To play the game:

1. Copy the code into a Python file (e.g., `space_invaders.py`).
2. Run the file with Python by typing `python space_invaders.py` in your terminal or command prompt.
3. Follow the instructions on the screen.

Remember, this is a very basic version of Space Invaders. For a more advanced game with graphics and more complex mechanics, you would typically use a library like Pygame.