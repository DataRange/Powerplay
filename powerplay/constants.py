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
        self.ITEM_PIXELS = 8
        self.ITEM_WIDTH = self.ITEM_TILE_WIDTH * self.ITEM_PIXELS

        self.INVENTORY_GUI_BORDER_WIDTH = 5
        self.INVENTORY_GUI_WIDTH = self.ITEM_WIDTH + (self.INVENTORY_GUI_BORDER_WIDTH * 2) + (self.ITEM_TILE_WIDTH * 2)
        self.INVENTORY_GUI_X = 25
        self.INVENTORY_GUI_Y = self.WINHEIGHT - (25 + self.INVENTORY_GUI_WIDTH)

        self.HOTBAR_ITEM_QUANTITY = 4

class Image_Maps:

    EMPTY_MAP = [
        [],
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    ]

    STICK_MAP = [
        [(205, 127, 50), (139, 69, 19)],
        [
            [0, 0, 0, 0, 0, 0, 2, 2],
            [0, 0, 0, 0, 0, 2, 1, 2],
            [0, 0, 0, 0, 2, 1, 2, 0],
            [0, 0, 0, 2, 1, 2, 0, 0],
            [0, 0, 2, 1, 2, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0, 0],
            [2, 1, 2, 0, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0, 0, 0],
        ]
    ]

    WOOD_MAP = [
        [(205, 127, 50), (139, 69, 19)],
        [
            [0, 0, 2, 2, 2, 2, 0, 0],
            [0, 2, 2, 1, 1, 2, 2, 0],
            [0, 2, 1, 1, 1, 1, 2, 0],
            [0, 2, 1, 1, 1, 1, 2, 0],
            [0, 2, 2, 1, 1, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 0],
            [0, 0, 2, 2, 2, 2, 0, 0],
        ]
    ]

    ROCK_MAP = [
        [(125, 125, 125), (75, 75, 75)],
        [
            [0, 0, 0, 2, 2, 2, 0, 0],
            [0, 0, 2, 1, 1, 1, 2, 0],
            [0, 2, 1, 1, 1, 1, 1, 2],
            [0, 2, 1, 1, 1, 2, 1, 2],
            [2, 1, 1, 2, 2, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 2, 0],
            [0, 2, 1, 1, 1, 2, 0, 0],
            [0, 0, 2, 2, 2, 0, 0, 0],
        ]
    ]