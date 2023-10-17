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

        #timer
        self.timers = {
            'Block falling' : Timer(GAME_UPDATE_SPEED, True, self.block_fall),
            'Horizontal movement' : Timer(INPUT_DELAY, False, self.player_input)
        }
        self.timers['Block falling'].activate()

        #tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

    def draw_grid(self):
        for i in range(1, GAME_HEIGHT):
            pygame.draw.line(self.image, 'white', (0, i*TILE_SIZE), (GAME_WIDTH, i*TILE_SIZE))
        for j in range(1, GAME_WIDTH):
            pygame.draw.line(self.image, 'white', (j*TILE_SIZE, 0), (j*TILE_SIZE, GAME_HEIGHT))

        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)        

    def block_fall(self):
        self.tetromino.block_fall()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['Horizontal movement'].activated:
            self.timers['Horizontal movement'].activate()
            if(keys[pygame.K_a]):
                self.tetromino.move_horizontal(-1)
            if(keys[pygame.K_d]):
                self.tetromino.move_horizontal(1)
            if(keys[pygame.K_s]):
                self.tetromino.block_fall()

    def update(self):
        #draw panel
        self.display.blit(self.image, self.rect)
        self.image.fill((40,40,40))

        #draw grid
        self.draw_grid()

        #draw tetrominos
        self.sprites.draw(self.image)
        
        #timers
        self.timers['Block falling'].update()
        self.timers['Horizontal movement'].update()

        #player input
        self.player_input()


class Tetromino():
    def __init__(self, shape, group):
        #general
        self.positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.image = [Block(pos, self.color, group) for pos in self.positions]

    def sides_colliding(self, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount)) for block in self.image]
        if any(collision_list):
            return True
        return False
    
    def bottom_colliding(self, amount):
        collision_list = [block.bottom_collide(int(block.pos.y + amount)) for block in self.image]
        if any(collision_list):
            return True
        return False

    def block_fall(self):
        if not self.bottom_colliding(1):
            for block in self.image:
                block.pos.y += 1
                block.update()

    def move_horizontal(self, amount):
        if not self.sides_colliding(amount):
            for block in self.image:
                block.pos.x += amount
                block.update()

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, color, group):
        super().__init__(group)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)

        self.pos = pygame.Vector2(pos) + pygame.Vector2(4,2)#offset
        self.rect = self.image.get_rect(topleft = (self.pos * TILE_SIZE)) 

    def horizontal_collide(self, x):
        if not 0 <= x < COL:
            return True
        
    def bottom_collide(self, y):
        if not y < ROW:
            return True

    def update(self):
        self.rect = self.image.get_rect(topleft = (self.pos * TILE_SIZE))

