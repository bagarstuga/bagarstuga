"""This module adresses the platforms and
   gives them some parameters to confide to"""
import pygame as pg
from settings import *
class Platform(pg.sprite.Sprite):
    """A class for how the platforms are to behave."""
    def __init__(self, x_pos, y_pos, width, height):
        """The platformns are created with its postition,
           height and width. It gets a color and the postition
           is specified. It also makes the class a sprite in
           pygame"""
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
