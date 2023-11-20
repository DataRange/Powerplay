import pygame
import numpy

class Player:

    def __init__(self, game):

        self.game = game
        self.window = game.window
        self.constants = game.constants

        self.rect = pygame.Rect(0, 0, self.constants.PLAYER_WIDTH, self.constants.PLAYER_WIDTH)

        self.x = 0
        self.y = 0

        self.x_velocity = 0
        self.y_velocity = 0

        self.player_right = False
        self.player_left = False
        self.player_up = False
        self.player_down = False

        self.hp = self.constants.MAX_HP

    def set_right(self, right): self.player_right = right
    def set_left(self, left): self.player_left = left
    def set_up(self, up): self.player_up = up
    def set_down(self, down): self.player_down = down

    def get_hp(self): return self.hp
    def get_coordinates(self): return (
        round(self.x/self.constants.PLAYER_WIDTH), 
        round(self.y/self.constants.PLAYER_WIDTH)
    )

    def get_rect(self): return self.rect

    def update(self):

        self.rect.x = self.x
        self.rect.y = self.y

        if self.player_right: self.x_velocity += 1
        elif self.player_left: self.x_velocity -= 1
        else:
            if abs(self.x_velocity) > 0: self.x_velocity += -1 if self.x_velocity > 0 else 1

        if self.player_up: self.y_velocity -= 1
        elif self.player_down: self.y_velocity += 1
        else:
            if abs(self.y_velocity) > 0: self.y_velocity += -1 if self.y_velocity > 0 else 1

        self.x_velocity = numpy.clip(self.x_velocity, -self.constants.MAX_PLAYER_VELOCITY, self.constants.MAX_PLAYER_VELOCITY)
        self.y_velocity = numpy.clip(self.y_velocity, -self.constants.MAX_PLAYER_VELOCITY, self.constants.MAX_PLAYER_VELOCITY)

        self.x += self.x_velocity
        self.y += self.y_velocity

    def draw(self):

        pygame.draw.rect(self.window, (255, 0, 0), self.rect)