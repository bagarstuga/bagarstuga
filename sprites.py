"""TODO"""
import pygame as pg
from settings import *

class shark(pg.sprite.Sprite):
    """TODO"""
    def __init__(self):
        """TODO"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCR_WIDTH / 2, SCR_HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        """TODO"""
        key_press = pg.key.get_pressed()
        if key_press[pg.K_LEFT]:
            self.vx = -3
        if key_press[pg.K_RIGHT]:
            self.vx = 3
        self.rect.x += self.vx
        self.rect.y += self.vy
