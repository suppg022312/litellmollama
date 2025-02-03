: Creating a full-fledged Asteroids game in Python and Streamlit is quite complex task. Here's an example of how you can get started with the basic structure using classes to define objects, functions for movements etc. 

```python
import streamlit as st
import random
from typing import List, Tuple

class Asteroid:
    def __init__(self, x: int, y: int):
        self.x = x  # asteroid's position on the X axis.
        self.y = y  # asteroid's position on the Y axis. 
                     # (0,0) is top left corner of Streamlit app window
class Ship:
    def __init__(self):
        self.x = random.randint(15, st.size[0] - 15)  # Random x position for the ship
        self.y = st.size[1]  # Position at the bottom of Streamlit app window
```
This is just a starting point and doesn't include any movement or collision detection logic yet. You would need to add those in order to make it into an actual game! 

Also, please note that Streamlit is not typically used for creating games due to its single-threaded nature which can lead to laggy performance when dealing with complex animations and computations required by a game like Asteroids. For more advanced or complex applications such as this one, it's recommended to use a dedicated game development environment/engine that was designed for these types of tasks.

Remember: This is just an example! You would need to add the logic yourself in order to make your program work correctly and have all the elements you want (score system, lives display etc).