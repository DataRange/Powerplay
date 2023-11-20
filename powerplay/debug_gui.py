import pygame

class DebugGUI:

    def __init__(self, game):

        self.game = game
        self.window = game.window
        self.constants = game.constants
        self.castle = game.castle
        self.player = game.player

        self.font = pygame.font.SysFont(self.constants.TEXT_FONT, self.constants.GUI_TEXT_SIZE, True)

        self.text = []

    def update(self):

        self.text = [
            f"HP: {self.castle.get_hp()}",
            f"X: {self.player.get_coordinates()[0]} Y: {self.player.get_coordinates()[1]}",
        ]

    def draw(self):

        y = 10
        for text in self.text:
            self.window.blit(self.font.render(text, 1, (0, 0, 0)), (10, y))
            y += 25