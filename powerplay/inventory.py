import pygame

class Inventory:

    def __init__(self, game):

        self.game = game
        self.window = game.window
        self.constants = game.constants

        self.inventory = []
        self.selected_item = None
        self.hotbar = []

    def get_inventory(self): return self.inventory

    def add_item(self, item): self.inventory.append(item)

    def clear_inventory(self): self.inventory = []

    def update(self):

        self.selected_item = self.inventory[0] if self.inventory else None
        self.hotbar = self.inventory[1:5]

    def draw(self):

        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(
            self.constants.INVENTORY_GUI_X, self.constants.INVENTORY_GUI_Y, 
            self.constants.INVENTORY_GUI_WIDTH, self.constants.INVENTORY_GUI_WIDTH),
            self.constants.INVENTORY_GUI_BORDER_WIDTH
        )

        if self.selected_item:
            self.selected_item.set_coordinates(
                self.constants.INVENTORY_GUI_X + self.constants.ITEM_TILE_WIDTH + self.constants.INVENTORY_GUI_BORDER_WIDTH,
                self.constants.INVENTORY_GUI_Y + self.constants.ITEM_TILE_WIDTH + self.constants.INVENTORY_GUI_BORDER_WIDTH
            )
            self.selected_item.draw()

        for i in range(self.constants.HOTBAR_ITEM_QUANTITY):
            x = self.constants.INVENTORY_GUI_X + ((i + 1) * (self.constants.INVENTORY_GUI_WIDTH + self.constants.ITEM_TILE_WIDTH)) + self.constants.INVENTORY_GUI_WIDTH / 2

            pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(
                x, self.constants.INVENTORY_GUI_Y, 
                self.constants.INVENTORY_GUI_WIDTH, self.constants.INVENTORY_GUI_WIDTH),
                self.constants.INVENTORY_GUI_BORDER_WIDTH
            )

            if i < len(self.hotbar):
                self.hotbar[i].set_coordinates(
                    x + self.constants.ITEM_TILE_WIDTH + self.constants.INVENTORY_GUI_BORDER_WIDTH,
                    self.constants.INVENTORY_GUI_Y + self.constants.ITEM_TILE_WIDTH + self.constants.INVENTORY_GUI_BORDER_WIDTH
                )
                self.hotbar[i].draw()