import pygame

class Forge:

    def __init__(self, game, coordinates):

        self.game = game
        self.window = game.window
        self.constants = game.constants

        self.colors = [(50, 50, 50), (100, 100, 100)]
        self.forge_img = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 2, 2, 1, 0, 0],
            [0, 1, 2, 2, 2, 2, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
        ]

        self.x = coordinates[0]
        self.y = coordinates[1]

    def draw(self):

        yPos = self.y
        for idy in self.forge_img:
            xPos = self.x
            for idx in idy:
                if idx > 0:
                    pygame.draw.rect(
                        self.window,
                        self.colors[idx - 1],
                        pygame.Rect(xPos, yPos, self.constants.ITEM_TILE_WIDTH, self.constants.ITEM_TILE_WIDTH)
                    )
                xPos += self.constants.ITEM_TILE_WIDTH
            yPos += self.constants.ITEM_TILE_WIDTH