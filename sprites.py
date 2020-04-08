import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        # pg.sprite.Sprite.sur
        self.image= pg.Surface((60,30))
        self.image.load("shark-facing-right.png")
