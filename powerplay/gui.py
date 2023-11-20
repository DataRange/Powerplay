import pygame

class GUI:

    def __init__(self, game, dimensions, bg_color, dat):

        self.game = game
        self.window = game.window
        self.constants = game.constants
        self.bg_color = bg_color

        self.data = dat

        self.dimensions = dimensions
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]
        
        self.gui = pygame.Rect(
            (self.constants.WINWIDTH - self.width) / 2,
            (self.constants.WINHEIGHT - self.height) / 2,
            self.width,
            self.height,
        ) # -700 -1400

    def draw(self):

        pygame.draw.rect(
            self.window,
            self.bg_color,
            self.gui,
            border_radius=self.constants.GUI_BORDER_RADIUS
        )

        if self.data:

            slots = self.data.get_slots()
            positions = self.data.get_positions()

            for position in positions: 

                x, y = position

                pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(
                    x, y, 
                    self.constants.INVENTORY_GUI_WIDTH, self.constants.INVENTORY_GUI_WIDTH),
                    self.constants.INVENTORY_GUI_BORDER_WIDTH
                )

class GUI_Data:

    def __init__(self, *args):

        self.slots = [None for _ in range(len(args))]
        self.positions = args

    def get_slots(self): return self.slots
    def get_positions(self): return self.positions

    def set_item(self, idx, item): self.slots[idx] = item
    def get_item(self, idx): return self.slots[idx]