"""TODO"""
import pygame as pg
import random
from sprites import *
from settings import *

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
        self.sprites = pg.sprite.Group()
        self.player = shark()
        self.sprites.add(self.player)
        self.events()
    def go(self):
        """TODO"""
        pass
    def update(self):
        """TODO"""
        self.sprites.update()
        pg.display.update()
    def events(self):
        """TODO"""
        while self.running:
            self.timing.tick(FPS)
            self.go()
            self.graphic()
            self.update()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
        pg.quit()
    def graphic(self):
        """TODO"""
        self.screen.fill(GREEN)
        self.sprites.draw(self.screen)
    def end_screen(self):
        """TODO"""
        pass
    def start_screen(self):
        """TODO"""
        pass

def main():
    """TODO"""
    m = main_class()
    m.start_screen()
    m.render()

if __name__== "__main__":
    main()

