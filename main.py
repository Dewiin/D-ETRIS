from settings import *
from sys import exit
from random import choice

from game import Game
from score import Score
from preview import Preview

class Main():
    def __init__(self):
        #general
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("D-ETRIS")
        self.clock = pygame.time.Clock()

        #create next shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for i in range(3)]

        #screen
        self.game_screen = Game(self.get_next_shape)
        self.score_screen = Score()
        self.preview_screen = Preview(self.next_shapes)
    
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            self.screen.fill(GRAY)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.game_screen.tetromino.rotate_left()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.game_screen.tetromino.rotate_right()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #screens
            self.game_screen.update()
            self.score_screen.update()
            self.preview_screen.update()

            #display
            pygame.display.update()

            self.clock.tick(60)      

if __name__ == '__main__':
    main = Main()
    main.run()