import pygame
import random
import math

class Enemy:
    def __init__(self, game, x, y):

        self.constants = game.constants 
        self.window = game.window

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.constants.PLAYER_WIDTH, self.constants.PLAYER_WIDTH)
        self.health = self.constants.BASE_ENEMY_HP


    def getDistance(self, x1, y1, x2, y2):
        return abs(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))
    
    def Death(self):
        self.health = 0

    def update(self):
        if(self.getDistance(self.x, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y) < 20):#implement a castle hp decrease here
            self.Death()

        else:   
            randomGen = random.randint(0,5)
            randomMove = random.randint(self.constants.MAX_ENEMY_MOVE - 2, self.constants.MAX_ENEMY_MOVE)
            if(randomGen < 2 and self.y > 20):
                self.y += randomMove
            else:
                if(self.getDistance(self.x + randomMove, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y) < self.getDistance(self.x - randomMove, self.y, self.constants.CASTLE_X, self.constants.CASTLE_Y)):
                    self.x += randomMove
                else:
                    self.x -= randomMove

    def draw(self):
        if(self.health > 0):
            self.window.blit(pygame.image.load("assets/Enemy_Melee.png"), (self.x+self.constants.SIDEBAR_WIDTH, self.y))
        