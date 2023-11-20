import sys
import pygame

from constants import Constants
from constants import Level_1
from player import Player
from debug_gui import DebugGUI
from inventory import Inventory
from enemy import Enemy
from items import *
from gui import GUI, GUI_Data
from castle import Castle

class App:

    def __init__(self):

        pygame.init()
        self.constants = Constants()
        self.level_1_constants = Level_1()

        self.window = pygame.display.set_mode((self.constants.WINWIDTH, self.constants.WINHEIGHT))
        pygame.display.set_caption("Powerplay")

        self.clock = pygame.time.Clock()

        self.player = Player(self)
        self.castle = Castle(self, self.level_1_constants.CASTLE_HP)
        self.debug = DebugGUI(self)
        self.inventory = Inventory(self)
        self.inventory.add_item(Wood(self))
        self.inventory.add_item(Rock(self))

        self.sidebar_dat = GUI_Data()
        self.sidebar = GUI(
            self,
            (200, self.constants.WINHEIGHT),
            (215, 215, 215),
            self.sidebar_dat,
            (0, 0)
        )

        self.tempEnemy = Enemy(self, 0, 0)
        self.enemies = []
        self.generateEnemies(self.level_1_constants.MELEE_ENEMY_X)

        self.show_gui = False
        self.init_gui()

        self.keybinds = {
            "right": pygame.K_RIGHT,
            "left": pygame.K_LEFT,
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "sidebar": pygame.K_TAB,
            "interact": pygame.K_SPACE
        }

    def init_gui(self):

        pass

    def run(self):

        while True:

            self.eventHandler()
            self.updateHandler()
            self.screenRefresh()

            self.clock.tick(60)

    def eventHandler(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == self.keybinds["right"]: self.player.set_right(True)

                elif event.key == self.keybinds["left"]: self.player.set_left(True)

                elif event.key == self.keybinds["up"]: self.player.set_up(True)

                elif event.key == self.keybinds["down"]: self.player.set_down(True)

                elif event.key == self.keybinds["sidebar"]: self.show_gui = True

            elif event.type == pygame.KEYUP:

                if event.key == self.keybinds["right"]: self.player.set_right(False)

                elif event.key == self.keybinds["left"]: self.player.set_left(False)

                elif event.key == self.keybinds["up"]: self.player.set_up(False)

                elif event.key == self.keybinds["down"]: self.player.set_down(False)

                elif event.key == self.keybinds["sidebar"]: self.show_gui = False

    def updateHandler(self):

        self.inventory.update()
        self.player.update()
        self.debug.update()
        for e in self.enemies:
            e.update()

    def screenRefresh(self):

        self.window.fill((200, 200, 200))
        self.castle.draw()
        for e in self.enemies:
            e.draw()
        self.player.draw()
        self.inventory.draw()

        if self.show_gui: self.sidebar.draw()

        self.player.draw()
        pygame.display.flip()

    def generateEnemies(self, list):
        for xCoord in list:
            self.tempEnemy = Enemy(self, xCoord, self.level_1_constants.MELEE_ENEMY_Y)
            self.enemies.append(self.tempEnemy)

if __name__ == '__main__':
    app = App()
    app.run()
