from settings import *
from sys import exit

from game import Game
from score import Score
from preview import Preview

class Main():
    def __init__(self):
        #general
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("D-ETRIS")

        #screen
        self.game_screen = Game()
        self.score_screen = Score()
        self.preview_screen = Preview()

    def run(self):
        while True:
            self.screen.fill((40,40,40))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #screens
            self.game_screen.update()
            self.score_screen.update()
            self.preview_screen.update()

            #display
            pygame.display.update()


        

if __name__ == '__main__':
    main = Main()
    main.run()