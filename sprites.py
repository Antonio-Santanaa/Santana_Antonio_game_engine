import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# where assets are taken from---------------------------------------------------------------------------------------------
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


# Making the character--------------------------------------------------------------------------------------------------
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder,'Orbo_Character.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.hitpoints = 5
        self.score = 0
# Character Controls---------------------------------------------------------------------------------------------------
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
        if keys[pg.K_e]:
            # self.dash_right()
            self.acc.x = +30
        if keys[pg.K_q]:
            # self.dash_left()
            self.acc.x = -30

    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        ghits = pg.sprite.collide_rect(self, self.game.ground)
        if hits or ghits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        #Checks if player collides with mobs----------------------------------------------------------------------------
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        #friction-------------------------------------------------------------------------------------------------------
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        mhits = pg.sprite.spritecollide(self, self.game.all_mobs, True)
        if mhits: 
            print("talk")
            self.game.score += 1
# platforms-------------------------------------------------------------------------------------------------------------

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.kind = kind
        self.image = pg.image.load(os.path.join(img_folder,'Orbo_Character.png')).convert()
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
# Background image------------------------------------------------------------------------------------------------------
class Scene(Sprite):
    def __init__(self, background):
        Sprite.__init__(self)
        self.background = background
        self.image = pg.image.load(os.path.join(img_folder,'space_background.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH, HEIGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        pass