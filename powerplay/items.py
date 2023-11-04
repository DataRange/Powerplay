import pygame

class Item:

    def __init__(self, game, item_map):

        self.game = game
        self.window = game.window
        self.constants = game.constants

        self.item_img = item_map

        self.x = 0
        self.y = 0

    def set_coordinates(self, x, y):
        
        self.x = x
        self.y = y

    def get_coordinates(self): return (self.x, self.y)

    def draw(self):

        idy = self.y
        for y in range(self.constants.ITEM_PIXELS):
            idx = self.x
            for x in range(self.constants.ITEM_PIXELS):
                pygame.draw.rect(
                    self.window, self.item_img[y][x][1], pygame.Rect(
                        idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                    ))
                idx += self.constants.ITEM_TILE_WIDTH
            idy += self.constants.ITEM_TILE_WIDTH