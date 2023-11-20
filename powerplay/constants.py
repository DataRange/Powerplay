class Constants:

    def __init__(self):

        self.WINWIDTH = 800
        self.WINHEIGHT = 600

        self.PLAYER_WIDTH = 50
        self.MAX_PLAYER_VELOCITY = 10
        self.MAX_HP = 100

        self.ENEMY_WIDTH = 100
        self.MAX_ENEMY_MOVE = 1
        self.BASE_ENEMY_HP = 1

        self.GUI_TEXT_SIZE = 28
        self.TEXT_FONT = "txt"
        self.GUI_BORDER_RADIUS = 3
        self.GUI_SIZE_STANDARD = (600, 480)

        self.ITEM_TILE_WIDTH = 5
        self.ITEM_PIXELS = 8
        self.ITEM_WIDTH = self.ITEM_TILE_WIDTH * self.ITEM_PIXELS

        self.INVENTORY_GUI_BORDER_WIDTH = 5
        self.INVENTORY_GUI_WIDTH = self.ITEM_WIDTH + (self.INVENTORY_GUI_BORDER_WIDTH * 2) + (self.ITEM_TILE_WIDTH * 2)
        self.INVENTORY_GUI_X = 265
        self.INVENTORY_GUI_Y = self.WINHEIGHT - (25 + self.INVENTORY_GUI_WIDTH)

        self.FORGE_GUI_X = int((self.WINWIDTH - self.GUI_SIZE_STANDARD[0]) / 2 + self.INVENTORY_GUI_WIDTH)
        self.FORGE_GUI_Y = int((self.WINHEIGHT - self.GUI_SIZE_STANDARD[1]) / 2 + self.INVENTORY_GUI_WIDTH)

        self.HOTBAR_ITEM_QUANTITY = 4

        self.SIDEBAR_WIDTH = 140
        self.SIDEBAR_HEIGHT = 800

        self.CASTLE_X = 250
        self.CASTLE_Y = 0
        
        self.INTERACT_FORGE = 0
        
class Level_1:
    def __init__(self):
        self.constants = Constants()

        self.CASTLE_HP = 10

        self.MELEE_ENEMY_X = [100,200,300,400,500,600]
        self.MELEE_ENEMY_Y = 400


        self.INTERACT_FORGE = 0

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

    ENEMY_MAP = [
        [(0,0,0), (215, 0, 0)],
        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1, 2, 1, 1],
            [1, 1, 2, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
    ]

    RETICLE_MAP = [
        [(225,0,0)],
        [
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
        ]
    ]