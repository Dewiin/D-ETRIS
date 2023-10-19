from settings import *

class Preview():
    def __init__(self, next_shapes):
        #general
        self.image = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION - PADDING))
        self.rect = self.image.get_rect(topleft = (PADDING*2 + GAME_WIDTH, PADDING))
        self.display = pygame.display.get_surface()

        #next shapes
        self.next_shapes = next_shapes
        self.preview_images = {shape: pygame.image.load(f'Graphics/{shape}.png').convert_alpha() for shape in TETROMINOS.keys()}


    def draw_shapes(self):
        #draw border and fill
        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)
        self.image.fill(GRAY)

        #show preview shapes
        #self.display.blit(self.preview_images[self.next_shapes[0]], self.preview_rect)

    def update(self):
        self.display.blit(self.image, self.rect)
        self.draw_shapes()