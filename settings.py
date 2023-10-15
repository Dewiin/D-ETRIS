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

TETROMINOS = {
    'T' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'L' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'J' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'S' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'Z' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'O' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
    'I' : {'shape' : [(-1,0),(0,0),(1,0),(0,-1)], 'color' : 'purple'},
}