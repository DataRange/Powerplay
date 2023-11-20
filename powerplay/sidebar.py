import pygame

#to display info like kills, wave num, etc.
class Sidebar:
    def __init__(self, game):

        self.window = game.window
        self.constants = game.constants
        
        self.rect = pygame.Rect(0, 0, self.constants.SIDEBAR_WIDTH, self.constants.SIDEBAR_HEIGHT)

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), self.rect)