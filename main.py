"""This module is the main module for the game
   Shark Rush. It starts the game and is the module where
   everything is connected. Run this module to start the game.
   The controls are simple. Arrow keys to move and spacebar to jump"""
import pygame as pg
import logging
from shark import *
from settings import *
from platforms import Platform

class MainClass:
    """This class contains methods for the start-screen,
       updating the screen, drawing sprites and the game loop"""
    def __init__(self):
        """This initializes pygame as well as the
           pygame mixer, which is used for playing sounds.
           Groups for platforms and sprites are made as to organize them.
           The clock tick is also set up."""
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pg.display.set_caption(TITLE)
        self.sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Shark()
        self.timing = pg.time.Clock()
        self.running = True
    def render(self):
        """When the game starts, create these first and play music,
           then go to the game loop in events(). Here the class Shark() is
           imported from sprites and becomes the player variable"""
        self.sprites.add(self.player)
        pg.mixer.music.load("FadeNCS.ogg")
        pg.mixer.music.play(-1)
        ground = Platform(0, SCR_HEIGHT - 30, SCR_WIDTH, 30)
        plat_1 = Platform(SCR_WIDTH / 2, 400, 200, 30)
        plat_2 = Platform(100, 600, 200, 30)
        plat_3 = Platform(100, 200, 200, 30)
        self.sprites.add(ground, plat_1, plat_2, plat_3)
        self.platforms.add(ground, plat_1, plat_2, plat_3)
        self.events()
    def update(self):
        """Updates the sprites and updates the screen"""
        self.sprites.update()
        collide = pg.sprite.spritecollide(self.player, self.platforms, False)
        if collide:
            self.player.pos.y = collide[0].rect.top
            self.player.vel.y = 0
        pg.display.flip()
    def events(self):
        """The game loop where the other methods are called and run
           until the end_game() method is called and running is false
           here the updating speed is set to the constant
           FPS"""
        while self.running:
            self.timing.tick(FPS)
            self.graphic()
            self.update()
            self.jumping_end_game()
        pg.quit()
    def graphic(self):
        """Draws the different sprites and the background"""
        background_img = pg.transform.scale\
        (pg.image.load("pool-water.jpg"), (SCR_WIDTH, SCR_HEIGHT))
        self.screen.blit(background_img, (0, 0))
        self.sprites.draw(self.screen)
    def jumping_end_game(self):
        """Makes use of the pygame.event.get() to
           both jump and see if the player wants to close
           the game, hence the name."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def start_screen(self):
        """This method defines two fonts, used for the two different
           text lines, these are put on top of the background,
           then checks if any key is pressed, if so, go to render(),
           otherwise, quit. There is a number 50 here, this is just a number
           which places the second line of text in a good place, right below
           the first line"""
        done = False
        font1 = pg.font.Font("freesansbold.ttf", 32)
        font2 = pg.font.Font("freesansbold.ttf", 20)
        text1 = font1.render("SharkRush", True, WHITE, BLUE)
        text_rect1 = text1.get_rect()
        text_rect1.center = (SCR_WIDTH / 2, SCR_HEIGHT / 2)
        text2 = font2.render("Press any key to continue", True, GREY, BLUE)
        text_rect2 = text2.get_rect()
        text_rect2.center = (SCR_WIDTH / 2, SCR_HEIGHT/ 2 + 50)
        while not done:
            self.screen.fill(BLUE)
            self.screen.blit(text1, text_rect1)
            self.screen.blit(text2, text_rect2)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYUP:
                    done = True
        self.render()
def main():
    """This function runs the method start_screen to display the start screen
       it is used to prevent global variables. It also contains
       the logging to see errors.
       """
    MainClass().start_screen()
    fmtstr = " %(asctime)s: (%(filename)s): %(levelname)s: %(funcName)s Line: %(lineno)d - %(message)s"
    datestr = "%m/%d/%y %I:%m:%S: %p "
    logging.basicConfig(
        filename= "custom_log_output.log",
        level= logging.DEBUG,
        filemode= "w",
        format= fmtstr,
        datefmt= datestr,
    )
    """different log messages"""
    logging.info("info message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("CRITICAL MESSAGE")
if __name__ == "__main__":
    main()

