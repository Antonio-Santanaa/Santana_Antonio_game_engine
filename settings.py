# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

import time
# cooldown for abilities 

# def cooldown()
#     cooldown = 0
#     if keys[pg.K_e]:

# if cooldown >= 0 

# game settings 
WIDTH = 1425
HEIGHT = 950
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"moving"),
                 (1200, 325, 120, 20, "moving", BLUE), 
                 (600, 250, 120, 20, "moving"),
                 (800, 160, 120, 20, "moving"),
                 (1200, 800, 120, 20, "moving"),
                 (125, HEIGHT - 350, 100, 20, "moving"),]
