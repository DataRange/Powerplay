import pygame
import numpy
from enemy import Enemy

class Spawner:
    def __init__(self, game, levelNum):
        self.window = game.window
        self.constants = game.constants
        self.clock = game.clock
        self.game = game
        
        self.xdict = game.xdict
        self.ydict = game.ydict
        self.enemies = game.enemies

        self.levelConstants = game.levels[levelNum - 1]
        
        self.lastSpawn = -self.levelConstants.ENEMY_DELAY * 1000
        self.delay = self.levelConstants.ENEMY_DELAY * 1000
        self.now = self.clock.get_time()

        self.maxEnemies = self.levelConstants.NUM_MELEE_ENEMIES
        self.count = 0

        self.over = False


    def update(self):
        self.now += self.clock.get_time()
        if(self.now - self.lastSpawn > self.delay and self.count < self.maxEnemies):
            self.game.addEnemy()
            self.lastSpawn = self.now
            self.count += 1

        elif(self.count == self.maxEnemies):
            for e in self.enemies:
                if(e.isDead() == False):
                    self.over = False
                else:  
                    self.over = True
    
    def isDone(self):
        return self.over