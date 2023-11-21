import pygame
import random
import math

from constants import Image_Maps

class Enemy:
    def __init__(self, game, x, y, curve_dict):

        self.constants = game.constants 
        self.window = game.window
        self.clock = game.clock

        self.castle = game.castle

        self.item_color = Image_Maps.ENEMY_MAP[0]
        self.item_img = Image_Maps.ENEMY_MAP[1]

        self.x = x
        self.y = y
        self.curve_dict = curve_dict

        self.rect = pygame.Rect(self.x, self.y, self.constants.PLAYER_WIDTH, self.constants.PLAYER_WIDTH)
        self.health = self.constants.BASE_ENEMY_HP


    def getDistance(self, x1, y1, x2, y2):
        return abs(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))
    
    def Death(self):
        self.health = 0

    def update(self):
        if(self.getDistance(self.x, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y) < 50 and self.health != 0):#implement a castle hp decrease here
            self.castle.hurt(self.health)
            self.Death()

        else:   
            #WPI new curve following code
            print("wow")

            #old random ai code
            '''randomGen = random.randint(0,9)
            randomMove = random.randint(self.constants.MAX_ENEMY_MOVE - 2, self.constants.MAX_ENEMY_MOVE)
            if(randomGen < 7):
                if(self.getDistance(self.x, self.y + randomMove, self.constants.CASTLE_X, self.constants.CASTLE_Y) < self.getDistance(self.x, self.y - randomMove, self.constants.CASTLE_X, self.constants.CASTLE_Y)):
                    self.y += randomMove
                else:
                    self.y -= randomMove
            else:
                if(self.getDistance(self.x + randomMove, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y) < self.getDistance(self.x - randomMove, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y)):
                    if(randomGen == 5):
                        randomMove + 10
                    self.x += randomMove
                else:
                    if(randomGen == 5):
                        randomMove + 10
                    self.x -= randomMove'''
            
    def draw(self):
        if(self.health > 0):
            idy = self.y-self.constants.ITEM_PIXELS
            for y in range(self.constants.ITEM_PIXELS):
                idx = self.x-self.constants.ITEM_PIXELS
                for x in range(self.constants.ITEM_PIXELS):
                    if self.item_img[y][x] > 0:
                        pygame.draw.rect(
                            self.window, self.item_color[self.item_img[y][x] - 1], pygame.Rect(
                                idx, idy, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH
                            ))
                    idx += self.constants.ITEM_TILE_WIDTH
                idy += self.constants.ITEM_TILE_WIDTH
