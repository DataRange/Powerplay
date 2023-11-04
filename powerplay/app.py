import sys
import pygame

from constants import Constants
from player import Player
from debug_gui import DebugGUI
from inventory import Inventory

class App:

    def __init__(self):

        pygame.init()
        self.constants = Constants()
        
        self.window = pygame.display.set_mode((self.constants.WINWIDTH, self.constants.WINHEIGHT))
        pygame.display.set_caption("Powerplay")

        self.clock = pygame.time.Clock()

        self.player = Player(self)
        self.debug = DebugGUI(self)
        self.inventory = Inventory(self)

        self.show_gui = False

    def run(self):

        while True:

            self.eventHandler()
            self.updateHandler()
            self.screenRefresh()

    def eventHandler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT: self.player.set_right(True)
                
                elif event.key == pygame.K_LEFT: self.player.set_left(True)

                elif event.key == pygame.K_UP: self.player.set_up(True)

                elif event.key == pygame.K_DOWN: self.player.set_down(True)

                elif event.key == pygame.K_TAB: self.show_gui = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT: self.player.set_right(False)
                
                elif event.key == pygame.K_LEFT: self.player.set_left(False)

                elif event.key == pygame.K_UP: self.player.set_up(False)

                elif event.key == pygame.K_DOWN: self.player.set_down(False)

                elif event.key == pygame.K_TAB: self.show_gui = False

    def updateHandler(self):

        self.player.update()
        self.debug.update()

    def screenRefresh(self):

        self.window.fill((200, 200, 200))
        self.player.draw()
        self.inventory.draw()

        if self.show_gui: self.debug.draw()
        pygame.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()