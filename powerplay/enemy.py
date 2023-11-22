import pygame
import random
import math

from constants import Image_Maps

class Enemy:
    def __init__(self, game, xdict, ydict):

        self.constants = game.constants 
        self.window = game.window
        self.clock = game.clock

        self.castle = game.castle

        self.item_color = Image_Maps.ENEMY_MAP[0]
        self.item_img = Image_Maps.ENEMY_MAP[1]

        self.x = 10000
        self.y = 10000
        self.xdict = xdict
        self.ydict = ydict

        self.rect = pygame.Rect(self.x, self.y, self.constants.PLAYER_WIDTH, self.constants.PLAYER_WIDTH)
        self.health = self.constants.BASE_ENEMY_HP

        self.last = 0
        self.speed = self.constants.ENEMY_MOVE_SPEED
        self.now = self.clock.get_time()
        self.count = 0


    def getDistance(self, x1, y1, x2, y2):
        return abs(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))
    
    def Death(self):
        self.health = 0

    def update(self):
        if(self.count == self.constants.ENEMY_PATH_DETAIL - 1 and self.health > 0):#implement a castle hp decrease here
            self.castle.hurt(self.health)
            self.Death()

        elif(self.health > 0):   
            #WIP new curve following code
            self.now += self.clock.get_time()
            if(self.now - self.last > self.speed):
                self.last = self.now
                self.x = self.xdict.get(self.count + 0.0)
                self.y = self.ydict.get(self.count + 0.0)
                self.count += 1

    def isDead(self):
        return self.health == 0

    def draw(self):
        if(self.health > 0):
            idy = self.y + 20
            for y in range(self.constants.ITEM_PIXELS):
                idx = self.x - 30
                for x in range(self.constants.ITEM_PIXELS):
                    if self.item_img[y][x] > 0:
                        pygame.draw.rect(
                            self.window, self.item_color[self.item_img[y][x] - 1], pygame.Rect(
                                idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                            ))
                    idx += self.constants.ITEM_TILE_WIDTH
                idy += self.constants.ITEM_TILE_WIDTH
