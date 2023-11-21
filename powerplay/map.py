import pygame
import numpy as np
from constants import Image_Maps

class Map:
    def __init__(self, game, curve_points):
        self.window = game.window
        self.constants = game.constants

        self.curve_points = curve_points

        self.item_color = Image_Maps.PATH_MAP[0]
        self.item_img = Image_Maps.PATH_MAP[1]

    def draw(self):
        p0 = self.curve_points[0]
        p1 = self.curve_points[1]
        p2 = self.curve_points[2]
        #quadratic bezier curve
        for t in np.arange(0, 1, 0.033):
            self.x = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
            self.y = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2  
            idy = self.y
            for y in range(len(self.item_img[1])):
                idx = self.x - 50
                for x in range(len(self.item_img[1])):
                    if self.item_img[y][x] > 0:
                        pygame.draw.rect(
                            self.window, self.item_color[self.item_img[y][x] - 1], pygame.Rect(
                                idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                            ))
                    idx += self.constants.ITEM_TILE_WIDTH
                idy += self.constants.ITEM_TILE_WIDTH