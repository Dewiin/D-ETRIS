from settings import *

class Preview():
    def __init__(self, next_shapes):
        #general
        self.image = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION - PADDING))
        self.rect = self.image.get_rect(topleft = (PADDING*3 + GAME_WIDTH + SIDEBAR_WIDTH, PADDING))
        self.display = pygame.display.get_surface()

        #next shapes
        self.next_shapes = next_shapes
        self.preview_images = {shape: pygame.image.load(f'../Graphics/{shape}.png').convert_alpha() for shape in TETROMINOS.keys()}

    def draw_shapes(self):
        #display preview shapes
        for i, shape in enumerate(self.next_shapes):
            preview_rects = self.preview_images[shape].get_rect(center = (self.image.get_width()/2, i * (self.image.get_height()/3) + 80))
            self.image.blit(self.preview_images[shape], preview_rects)

    def update(self):
        self.display.blit(self.image, self.rect)

        #draw border and fill
        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)
        self.image.fill(GRAY)

        #display preview shapes
        self.draw_shapes()