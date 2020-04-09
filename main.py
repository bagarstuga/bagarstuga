"""TODO"""
import pygame as pg
import random
from sprites import *
from settings import *
from fysik import *

class main_class:
    """TODO"""
    def __init__(self):
        """TODO"""
        pg.init()
        self.screen = pg.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pg.display.set_caption(TITLE)
        self.timing = pg.time.Clock()
        self.running = True
    def render(self):
        """TODO"""
        sprites = pg.sprite.Group()
    def go(self):
        """TODO"""
        self.going = True
        while self.going:
            self.update()
            self.events()
            self.graphic()
    def update(self):
        pass


        """TODO"""

        self.sprites.update()
    def events(self):
        """TODO"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.going:
                    self.going = False
                self.running = False
    def graphic(self):
        """TODO"""
        # self.screen.fill(GREEN)
        self.sprites.draw(self.screen)
    def end_screen(self):
        """TODO"""

    def start_screen(self):
        """TODO"""
m = main_class()
m.start_screen()
clock = pg.time.Clock()

while m.running:
    pg.event.get()
    m.render()
    m.end_screen()
    m.screen.fill((GREEN))
    pg.display.flip()
    clock.tick(30)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if self.going:
                self.going = False
            self.running = False




pg.quit()
