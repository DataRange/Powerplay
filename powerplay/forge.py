import pygame

class Forge:

    def __init__(self, game, coordinates):

        self.game = game
        self.window = game.window
        self.constants = game.constants
        self.player = game.player

        self.colors = [(50, 50, 50), (100, 100, 100)]
        self.forge_img = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 2, 2, 1, 0, 0],
            [0, 1, 1, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
        ]

        self.x = coordinates[0]
        self.y = coordinates[1]
        self.hitbox = pygame.Rect(
            self.x - (2 * self.constants.ITEM_TILE_WIDTH), 
            self.y - (2 * self.constants.ITEM_TILE_WIDTH), 
            self.constants.ITEM_WIDTH + (4 * self.constants.ITEM_TILE_WIDTH), 
            self.constants.ITEM_WIDTH + (4 * self.constants.ITEM_TILE_WIDTH)
        )

    def collides_with_player(self): return self.hitbox.colliderect(self.player.get_rect())

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

        if self.collides_with_player(): pygame.draw.rect(self.window, (255, 255, 255), self.hitbox, self.constants.ITEM_TILE_WIDTH)