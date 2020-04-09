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
            self.timing.tick(FPS)
            self.update()
            self.events()
            self.graphic()
    def update(self):
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
        self.screen.fill(GREEN)
        self.sprites.draw(self.screen)
        pg.display.flip()
    def end_screen(self):
        """TODO"""
        pass
    def start_screen(self):
        """TODO"""
        pass
m = main_class()
m.start_screen()
while m.running:
    m.render()
    m.end_screen()
    
pg.quit()
