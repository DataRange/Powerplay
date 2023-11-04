import pygame

class Inventory:

    def __init__(self, game):

        self.game = game
        self.window = game.window
        self.constants = game.constants

        self.inventory = []

    def get_inventory(self): return self.inventory

    def draw(self):

        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(
            self.constants.INVENTORY_GUI_X, self.constants.INVENTORY_GUI_Y, 
            self.constants.INVENTORY_GUI_WIDTH, self.constants.INVENTORY_GUI_WIDTH),
            self.constants.INVENTORY_GUI_BORDER_WIDTH
        )