"""TODO"""
import random
import pygame as pg
from sprites import *
from settings import *

class MainClass:
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
        self.player = Shark()
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
            self.end_game()
            pg.display.flip()
        pg.quit()
    def graphic(self):
        """TODO"""
        self.screen.fill(GREEN)
        self.sprites.draw(self.screen)
    def end_screen(self):
        """TODO"""
        pass
    def end_game(self):
        """TODO"""
        for event in pg.event.get():
             if event.type == pg.QUIT:
                 self.running = False
                 self.done = True
    def start_screen(self):
        """TODO"""
        done = False
        font1 = pg.font.Font("freesansbold.ttf", 32)
        font2 = pg.font.Font("freesansbold.ttf", 20)
        text1 = font1.render("SharkRush", True, WHITE, BLUE)
        text_rect1 = text1.get_rect()
        text_rect1.center = (SCR_WIDTH / 2, SCR_HEIGHT / 2)
        text2 = font2.render("Press any key to continue", True, GREY, BLUE)
        text_rect2 = text2.get_rect()
        text_rect2.center = (SCR_WIDTH / 2, SCR_HEIGHT/ 1.8)
        while not done:
            self.screen.fill(BLUE)
            self.screen.blit(text1, text_rect1)
            self.screen.blit(text2, text_rect2)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYUP:
                    done = True
                elif event.type == pg.QUIT:
                    pg.quit()
                    quit()
        self.render()
def main():
    """TODO"""
    m = MainClass()
    m.start_screen()
    

if __name__== "__main__":
    main()


