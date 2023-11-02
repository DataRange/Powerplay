import sys
import pygame

from constants import Constants

class App:

    def __init__(self):

        pygame.init()
        self.constants = Constants()
        
        self.window = pygame.display.set_mode((self.constants.WINWIDTH, self.constants.WINHEIGHT))
        pygame.display.set_caption("Powerplay")

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    app = App()
    app.run()