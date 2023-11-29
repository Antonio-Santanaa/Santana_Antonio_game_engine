# content from kids can code: http://kidscancode.org/blog/
# https://stackoverflow.com/questions/73307069/init-takes-6-positional-arguments-but-7-were-given 
# https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame 
# Goals: Make someone to  interact with; Catch all the cubes
# Rule: Jump and Run 
# feedback: score, health, points, mobs 
# Freeedom can run up, down, side to side
# mobs only move when you move 

# In the form of a sprite 
# Have platforms scroll left when I move right, like super mario.
# While self x+1 platforms x - 1

# Have obstacles that bounce the player backwards from the part of collision
# if collide Set.Player.pos x - 1 

# import libraries and modules-----------------------------------------------------------------------------------------
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

vec = pg.math.Vector2

# folders where assests are drawn from---------------------------------------------------------------------------------
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # initiates pygame and makes the window appear------------------------------------------------------------------
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self): 
        # all sprite groups--------------------------------------------------------------------------------------------
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes------------------------------------------------------------------------------------------
        self.player = Player(self)
        # add instances to groups---------------------------------------------------------------------------------------
        self.all_sprites.add(self.player)
        self.ground = Platform(*GROUND)
        self.all_sprites.add(self.ground)

        for p in PLATFORM_LIST:
            # instantiate platforms as class---------------------------------------------------------------------------
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        # mobs---------------------------------------------------------------------------------------------------------
        for m in range(0,10):
            m = Mob(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)

    
    def run(self):
        self.playing = True
        while self.playing:
            self.screen.blit(Scene, (0, 0))

            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
         # This makes it so that the character does not phase through platforms-----------------------------------------
        hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
        ghits = pg.sprite.collide_rect(self.player, self.ground)
        if hits or ghits:
            if self.player.vel.y < 0:
                self.player.vel.y = -self.player.vel.y
            # Stops player from falling through platforms---------------------------------------------------------------
            elif self.player.vel.y > 0:
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.5
                if ghits:
                    self.player.pos.y = self.ground.rect.top
                    self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
        # checks if window is closed and if it is, stop
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
# draw------------------------------------------------------------------------------------------------------------------ 
    def draw(self):
        # draw the background screen
        self.screen.fill(BLACK)
        # bg = pg.image.load("bg.png")

        # #INSIDE OF THE GAME LOOP
        # self.screen.blit(bg, (0, 0))
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Hitpoints: " + str(self.player.hitpoints), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
