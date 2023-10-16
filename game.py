from settings import *
from random import choice

from dropTimer import Timer

class Game():
    def __init__(self):
        #general
        self.image = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) #initialize display surface
        self.rect = self.image.get_rect(topleft = (PADDING, PADDING))
        self.display = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

        #grid color
        self.image.fill((40,40,40))

        #tetromino
        self.tetrominos = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

    def draw_grid(self):
        for i in range(1, GAME_HEIGHT):
            pygame.draw.line(self.image, 'white', (0, i*TILE_SIZE), (GAME_WIDTH, i*TILE_SIZE))
        for j in range(1, GAME_WIDTH):
            pygame.draw.line(self.image, 'white', (j*TILE_SIZE, 0), (j*TILE_SIZE, GAME_HEIGHT))

        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)        

    def update(self):
        #draw panel
        self.display.blit(self.image, self.rect)

        #draw grid
        self.draw_grid()

        #draw tetrominos
        self.sprites.draw(self.image)
    

class Tetromino():
    def __init__(self, shape, group):
        #general
        self.positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.image = [Block(pos, self.color, group) for pos in self.positions]

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, color, group):
        super().__init__(group)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))

        self.pos = pygame.Vector2(pos) + pygame.Vector2(4,0)#offset
        self.rect = self.image.get_rect(topleft = self.pos * TILE_SIZE)
        self.image.fill(color)
