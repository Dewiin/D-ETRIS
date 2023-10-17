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

#Window size
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + (PADDING*3)
WINDOW_HEIGHT = GAME_HEIGHT + (PADDING*2)

#Timer variables
GAME_UPDATE_SPEED = 800
INPUT_DELAY = 80

#Tetromino shapes
TETROMINOS = {
    'T' : {'shape' : [(-1,-1),(1,-1),(0,-1),(0,-2)], 'color' : 'purple'},
    'J' : {'shape' : [(-1,-2),(0,-2),(1,-2),(1,-1)], 'color' : 'blue'},
    'L' : {'shape' : [(-1,-1),(-1,-2),(0,-2),(1,-2)], 'color' : 'orange'},
    'Z' : {'shape' : [(-1,-2),(0,-2),(0,-1),(1,-1)], 'color' : 'red'},
    'S' : {'shape' : [(-1,-1),(0,-1),(0,-2),(1,-2)], 'color' : 'green'},
    'O' : {'shape' : [(0,-1),(1,-1),(0,-2),(1,-2)], 'color' : 'yellow'},
    'I' : {'shape' : [(-1,-1),(0,-1),(1,-1),(2,-1)], 'color' : 'cyan'},
}

#Scoring
SCORE = {1:100, 2:300, 3:500, 4:1200}