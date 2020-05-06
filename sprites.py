"""TODO"""
import pygame as pg
from settings import *

class Shark(pg.sprite.Sprite):
    """TODO"""
    def __init__(self):
        """TODO"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale\
        (pg.image.load("shark-facing-right.png"),(PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCR_WIDTH / 2, SCR_HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        """TODO"""
        key_press = pg.key.get_pressed()
        if key_press[pg.K_LEFT]:
            self.vx = -PLAYER_MVMNTSPEED
        if key_press[pg.K_RIGHT]:
            self.vx = PLAYER_MVMNTSPEED
        self.rect.x += self.vx
        self.rect.y += self.vy

