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
        self.game_active = True
        self.game_over_screen = pygame.image.load('../Screens/gameover.png').convert()
        self.game_over_screen = pygame.transform.rotozoom(self.game_over_screen, 0, 0.5)
        self.restart_button = pygame.Rect(393, 440, TILE_SIZE*2, TILE_SIZE*2)

        #create next shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for i in range(3)]

        #holding
        self.first_hold = True
        self.hold_limit = False

        #screens
        self.score_screen = Score()
        self.game_screen = Game(self.get_next_shape, self.score_screen.scoring_info, self.set_game_active)
        self.preview_screen = Preview(self.next_shapes)
        self.hold_queue = Hold_Queue()

        #sound
        self.game_music = pygame.mixer.Sound('../Sound/PHONK.mp3')
        self.game_music.play(-1)
        self.game_over_sound = pygame.mixer.Sound('../Sound/game-over.mp3')
        self.game_over_sound.set_volume(0.1)

        self.game_over_played = False
    
    def set_game_active(self, bool):
        self.game_active = bool

    def game_over(self):
        if not self.game_over_played:
            self.game_over_played = True
            self.game_over_sound.play()
        self.screen.blit(self.game_over_screen, (-12,1))

    def get_next_shape(self):
        if not self.first_hold: self.hold_limit = False
        if self.game_screen.hold_queue: self.first_hold = False
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        
        return next_shape

    def run(self):
        while True:
            self.screen.fill(GRAY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.game_active:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        self.game_screen.tetromino.rotate_left()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        self.game_screen.tetromino.rotate_right()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not self.hold_limit:
                        self.hold_limit = True
                        self.game_screen.hold(self.hold_queue.get_shape)
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.restart_button.collidepoint(pygame.mouse.get_pos()):
                        self.hold_queue.shape = ''
                        self.first_hold = True
                        self.game_over_played = False
                        self.game_active = True
            
            if self.game_active:
                #music
                self.game_music.set_volume(0.3)

                #screens
                self.game_screen.update()
                self.score_screen.update()
                self.preview_screen.update()
                self.hold_queue.update()

            else:
                self.game_music.set_volume(0)
                self.game_over()

            #display
            pygame.display.update()

            self.clock.tick(60)      

if __name__ == '__main__':
    main = Main()
    main.run()