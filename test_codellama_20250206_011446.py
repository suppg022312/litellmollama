
Certainly! Here is an example of a simple asteroids game written in Python:
```
import turtle

# Set up the screen and background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a player object
player = turtle.Turtle()
player.shape("circle")
player.color("white")
player.speed(0)
player.penup()
player.goto(0, 0)

# Create an asteroid object
asteroid = turtle.Turtle()
asteroid.shape("square")
asteroid.color("red")
asteroid.speed(0)
asteroid.penup()
asteroid.goto(100, 100)

# Set up the game loop
while True:
    # Move the player and check for collisions with the asteroid
    player.forward(5)
    if player.distance(asteroid) < 20:
        print("Collision!")
        break
    
    # Update the screen and wait for a frame
    turtle.update()
```
This code creates a simple game where the player can move around on the screen using the arrow keys, and must avoid colliding with an asteroid that is randomly generated on the screen. The game loop updates the screen and checks for collisions between the player and the asteroid every frame. If there is a collision, the game ends and the player loses.

You can add more features to the game by adding more code, such as different shapes for the asteroids, different colors for the player, and more complex collision detection. You can also make the game more challenging by increasing the speed of the player or making the asteroid move faster.

I hope this helps! Let me know if you have any questions.