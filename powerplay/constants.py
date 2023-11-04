class Constants:

    def __init__(self):

        self.WINWIDTH = 800
        self.WINHEIGHT = 600

        self.PLAYER_WIDTH = 50
        self.MAX_PLAYER_VELOCITY = 10
        self.MAX_HP = 100

        self.GUI_TEXT_SIZE = 28
        self.TEXT_FONT = "txt"

        self.ITEM_TILE_WIDTH = 5
        self.ITEM_PIXELS = 5
        self.ITEM_WIDTH = self.ITEM_TILE_WIDTH * self.ITEM_PIXELS

        self.INVENTORY_GUI_BORDER_WIDTH = 5
        self.INVENTORY_GUI_WIDTH = self.ITEM_WIDTH + (self.INVENTORY_GUI_BORDER_WIDTH * 2)
        self.INVENTORY_GUI_X = 25
        self.INVENTORY_GUI_Y = self.WINHEIGHT - (25 + self.INVENTORY_GUI_WIDTH)