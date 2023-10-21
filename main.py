from settings import *
from sys import exit
from random import choice

from game import Game
from score import Score
from preview import Preview
from hold_queue import Hold_Queue

class Main():
    def __init__(self):
        #general
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("D-ETRIS")
        self.clock = pygame.time.Clock()

        #create next shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for i in range(3)]

        #holding
        self.first_hold = True
        self.hold_limit = False

        #screens
        self.score_screen = Score()
        self.game_screen = Game(self.get_next_shape, self.score_screen.scoring_info)
        self.preview_screen = Preview(self.next_shapes)
        self.hold_queue = Hold_Queue()

        #sound
        self.game_music = pygame.mixer.Sound('Sound/music.wav')

        self.game_music.set_volume(0.1)
        self.game_music.play(-1)
    
    def get_next_shape(self):
        if not self.first_hold:
            self.hold_limit = False
        self.first_hold = False
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not self.hold_limit:
                    self.hold_limit = True
                    self.game_screen.hold(self.hold_queue.get_shape)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #screens
            self.game_screen.update()
            self.score_screen.update()
            self.preview_screen.update()
            self.hold_queue.update()

            #display
            pygame.display.update()

            self.clock.tick(60)      

if __name__ == '__main__':
    main = Main()
    main.run()