"""This module adresses the platforms and
   gives them some parameters to confide to"""
import pygame as pg
from settings import *
class Platform(pg.sprite.Sprite):
    """The class which contain the init method that
       puts these parameters in place when initialized"""
    def __init__(self, x_pos, y_pos, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
