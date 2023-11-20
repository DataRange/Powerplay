import pygame

from constants import Image_Maps

class Castle:
    def __init__(self, game, health):
        self.constants = game.constants
        self.window = game.window
        self.clock = game.clock

        self.item_color = Image_Maps.CASTLE_MAP[0]
        self.item_img = Image_Maps.CASTLE_MAP[1]

        self.health = health
        self.x = self.constants.CASTLE_X
        self.y = self.constants.CASTLE_Y

        self.cooldown = 3
        self.last = -300
    
    def hurt(self, dmg):
        self.health -= dmg
        self.last = self.clock.get_time()

    def draw(self):
        now = self.clock.get_time()
        print(now)
        if ((now - self.last) < self.cooldown):
            self.item_color = Image_Maps.HURT_CASTLE_MAP[0]
        else:
            self.item_color = Image_Maps.CASTLE_MAP[0]
        if(self.health > 0):
            idy = self.y
            for y in range(len(self.item_img[1])):
                idx = self.x
                for x in range(len(self.item_img[1])):
                    if self.item_img[y][x] > 0:
                        pygame.draw.rect(
                            self.window, self.item_color[self.item_img[y][x] - 1], pygame.Rect(
                                idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                            ))
                    idx += self.constants.ITEM_TILE_WIDTH
                idy += self.constants.ITEM_TILE_WIDTH