from settings import *
from random import choice

from dropTimer import Timer

class Game():
    def __init__(self, get_next_shape, scoring_info):
        #general
        self.image = pygame.Surface((GAME_WIDTH, GAME_HEIGHT)) #initialize display surface
        self.rect = self.image.get_rect(topleft = (PADDING, PADDING))
        self.display = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.game_speed = GAME_UPDATE_SPEED

        #next_shape
        self.get_next_shape = get_next_shape

        #timer
        self.timers = {
            'Block falling' : Timer(self.game_speed, True, self.block_fall),
            'Horizontal movement' : Timer(INPUT_DELAY, False, self.player_input)
        }
        self.timers['Block falling'].activate()

        #field data
        self.field_data = [[0 for i in range(COL)] for j in range(ROW)]

        #tetromino
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino, self.field_data)

        #score
        self.level = 1
        self.score = 0
        self.lines_cleared = 0
        self.scoring_info = scoring_info

    def draw_grid(self):
        for i in range(1, GAME_HEIGHT):
            pygame.draw.line(self.image, GRAY, (0, i*TILE_SIZE), (GAME_WIDTH, i*TILE_SIZE))
        for j in range(1, GAME_WIDTH):
            pygame.draw.line(self.image, GRAY, (j*TILE_SIZE, 0), (j*TILE_SIZE, GAME_HEIGHT))

        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)        

    def calculate_score(self, lines_cleared):
        self.lines_cleared += lines_cleared
        if lines_cleared > 0: self.score += (SCORE[lines_cleared] * self.level)
        if self.lines_cleared / 10 > self.level:
            self.level += 1
            self.game_speed *= .8
            self.timers['Block falling'].cooldown = self.game_speed

        self.scoring_info(int(self.score), int(self.level), self.lines_cleared)
        
    def create_new_tetromino(self):
        self.check_rows()
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites, self.create_new_tetromino, self.field_data)

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
        
        self.calculate_score(len(deleted_rows))
        
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
        #check if at floor
        if not self.bottom_colliding(1):
            #drop tetromino
            for block in self.image:
                block.pos.y += 1
        else:
            #if at floor, add block positions into field_data
            for block in self.image:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            #create new tetromino
            self.create_new_tetromino()

    def move_horizontal(self, amount):
        #check if at edge
        if not self.sides_colliding(amount):
            #move horizontal
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

        self.pos = pygame.Vector2(pos) + pygame.Vector2(4,2)#offset
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

