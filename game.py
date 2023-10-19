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
            'Horizontal movement' : Timer(INPUT_DELAY, False, self.player_input),
            'Rotation' : Timer(ROTATE_DELAY)
        }
        self.timers['Block falling'].activate()

        #field data
        self.field_data = [[0 for i in range(COL)] for j in range(ROW)]

        #tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)

    def draw_grid(self):
        for i in range(1, GAME_HEIGHT):
            pygame.draw.line(self.image, 'white', (0, i*TILE_SIZE), (GAME_WIDTH, i*TILE_SIZE))
        for j in range(1, GAME_WIDTH):
            pygame.draw.line(self.image, 'white', (j*TILE_SIZE, 0), (j*TILE_SIZE, GAME_HEIGHT))

        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)        

    def create_new_tetromino(self):
        self.check_rows()
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)

    def block_fall(self):
        self.tetromino.block_fall()

    def player_input(self):
        keys = pygame.key.get_pressed()

        #movement
        if not self.timers['Horizontal movement'].activated:
            if keys[pygame.K_a]:
                self.tetromino.move_horizontal(-1)
                self.timers['Horizontal movement'].activate()
            if keys[pygame.K_d]:
                self.tetromino.move_horizontal(1)
                self.timers['Horizontal movement'].activate()
            if keys[pygame.K_s]:
                self.tetromino.block_fall()
                self.timers['Horizontal movement'].activate()

        #rotation
        if not self.timers['Rotation'].activated:
            if keys[pygame.K_RIGHT]:
                self.tetromino.rotate_right()
                self.timers['Rotation'].activate()
            if keys[pygame.K_LEFT]:
                self.tetromino.rotate_left()
                self.timers['Rotation'].activate()

    def check_rows(self):
        deleted_rows = []
        for row, row_values in enumerate(self.field_data):
            if all(row_values):
                deleted_rows.append(row)

        if deleted_rows:
            for delete_row in deleted_rows:

                #delete full rows
                for block in self.field_data[delete_row]:
                    block.kill()

                #move blocks down
                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y <= delete_row:
                            block.pos.y += 1  

            #rebuild field
            self.field_data = [[0 for i in range(COL)] for j in range(ROW)]
        
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
        
    def update(self):
        #draw panel
        self.display.blit(self.image, self.rect)
        self.image.fill(GRAY)

        #draw and update tetrominos
        self.sprites.update()
        self.sprites.draw(self.image)

        #draw grid
        self.draw_grid()
        
        #timers
        self.timers['Block falling'].update()
        self.timers['Horizontal movement'].update()
        self.timers['Rotation'].update()

        #player input
        self.player_input()

class Tetromino():
    def __init__(self, shape, group, create_new, field_data):
        #general
        self.shape = shape
        self.positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.field_data = field_data
        self.image = [Block(pos, self.color, group) for pos in self.positions]
        self.create_new_tetromino = create_new

    def sides_colliding(self, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.image]
        if any(collision_list):
            return True
        return False
    
    def bottom_colliding(self, amount):
        collision_list = [block.bottom_collide(int(block.pos.y + amount), self.field_data) for block in self.image]
        if any(collision_list):
            return True
        return False
    
    def block_fall(self):
        if not self.bottom_colliding(1):
            for block in self.image:
                block.pos.y += 1
        else:
            for block in self.image:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

    def move_horizontal(self, amount):
        if not self.sides_colliding(amount):
            for block in self.image:
                block.pos.x += amount

    def rotate_right(self):
        if self.shape != 'O':
            #pivot point
            pivot = self.image[2].pos

            #new_block_positions
            new_block_positions = [block.rotate_right(pivot) for block in self.image]

            #collision check
            for pos in new_block_positions:
                #horizontal
                if not 0 <= pos.x < COL:
                    return
                #field
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                #vertical
                if not pos.y < ROW:
                    return

            #implement new positions
            for i, block in enumerate(self.image):
                block.pos = new_block_positions[i]

    def rotate_left(self):
        if self.shape != 'O':
            #pivot point
            pivot = self.image[2].pos

            #new block positions
            new_block_positions = [block.rotate_left(pivot) for block in self.image]

            #collision check
            for pos in new_block_positions:
                #horizontal
                if not 0 <= pos.x < COL:
                    return
                #field
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                #vertical
                if not pos.y < ROW:
                    return    
        
            #implement new positions
            for i, block in enumerate(self.image):
                block.pos = new_block_positions[i]

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, color, group):
        super().__init__(group)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)

        self.pos = pygame.Vector2(pos) + pygame.Vector2(4,0)#offset
        self.rect = self.image.get_rect(topleft = (self.pos * TILE_SIZE)) 

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COL:
            return True
        if field_data[int(self.pos.y)][x]:
            return True
        
    def bottom_collide(self, y, field_data):
        if not y < ROW:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True

    def rotate_right(self, pivot):
        return pivot + (self.pos - pivot).rotate(90)
    
    def rotate_left(self, pivot):
        return pivot + (self.pos - pivot).rotate(-90)

    def update(self):
        self.rect = self.image.get_rect(topleft = (self.pos * TILE_SIZE))

