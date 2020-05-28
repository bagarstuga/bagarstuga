"""This module is for how the player or as we call
   it "shark" is to work andsays how it should works
   in regards to the other peices of the game"""
import pygame as pg
from settings import *
from main import *
class Shark(pg.sprite.Sprite):
    """The class Shark is a sprite in pygame and
       declares the variable vec for the class. This
       is used for vector 2. This makes acceleration work
       in two axis. X and Y, in other words, up and down."""
    vec = pg.math.Vector2
    def __init__(self):
        """Initializes the class and makes it a sprite in pygame.
           """
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale\
        (pg.image.load("shark-facing-right.png"),(PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCR_WIDTH / 2, SCR_HEIGHT - 30)
        self.pos = self.vec(SCR_WIDTH / 2, SCR_HEIGHT - 30)
        self.vel = self.vec(0, 0)
        self.acc = self.vec(0, 0)
    def jump(self):
        """This just makes the playes velocity upwards
           to the constant PLAYER_JUMPHEIGHT."""
        self.vel.y = PLAYER_JUMPHEIGHT
    def update(self):
        """Here the equations of motion are set and
           how the players postion is calculated.
           It uses the vector 2 that pygame comes with
           This way the motion feels more natural. Here
           the method checks if the player presses the arrow
           keys and gives momentum to the shark if so. It also
           constrains the shark to the borders of the screen.
           It also makes it so that the players rectangle is
           at the bottom, this way it is easier with collision.
           """
        self.acc = self.vec(0, GRAV_FRC)
        key_press = pg.key.get_pressed()
        if key_press[pg.K_LEFT]:
            self.acc.x = -PLAYER_MVMNTSPEED
        if key_press[pg.K_RIGHT]:
            self.acc.x = PLAYER_MVMNTSPEED
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > SCR_WIDTH:
            self.pos.x = SCR_WIDTH - 1
        if self.pos.x < 0:
            self.pos.x = 1
        self.rect.midbottom = self.pos
