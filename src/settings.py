import pygame

#Game size
ROW, COL = 20, 10
TILE_SIZE = 35
GAME_WIDTH, GAME_HEIGHT = 10 * TILE_SIZE, 20 * TILE_SIZE
PADDING = 20

#Sidebar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 0.3
HOLD_QUEUE_FRACTION = 0.3

#Window size
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH*2 + (PADDING*4)
WINDOW_HEIGHT = GAME_HEIGHT + (PADDING*2)

#Timer variables
GAME_UPDATE_SPEED = 1000
INPUT_DELAY = 50

#Colors
YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204b9b'
GREEN = '#65b32e'
PURPLE = '#7b217f'
CYAN = '#6cc6d9'
ORANGE = '#f07e13'
GRAY = '#282828'

#Tetromino shapes
TETROMINOS = {
    'T' : {'shape' : [(-1,-1),(1,-1),(0,-1),(0,-2)], 'color' : PURPLE},
    'J' : {'shape' : [(-1,-2),(1,-2),(0,-2),(1,-1)], 'color' : BLUE},
    'L' : {'shape' : [(-1,-1),(-1,-2),(0,-2),(1,-2)], 'color' : ORANGE},
    'Z' : {'shape' : [(-1,-2),(0,-2),(0,-1),(1,-1)], 'color' : RED},
    'S' : {'shape' : [(-1,-1),(0,-2),(0,-1),(1,-2)], 'color' : GREEN},
    'O' : {'shape' : [(0,-1),(1,-1),(0,-2),(1,-2)], 'color' : YELLOW},
    'I' : {'shape' : [(-1,-1),(1,-1),(0,-1),(2,-1)], 'color' : CYAN},
}

#Scoring
SCORE = {1:100, 2:300, 3:500, 4:1200}