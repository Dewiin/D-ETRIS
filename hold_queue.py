from settings import *

class Hold_Queue():
    def __init__(self):
        #general
        self.image = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*HOLD_QUEUE_FRACTION))
        self.rect = self.image.get_rect(topleft = (PADDING, PADDING))
        self.display_surface = pygame.display.get_surface()
        self.shape = ''

        #font
        self.font = pygame.font.Font('Graphics/Russo_One.ttf', 30)
        self.queue_surface = self.font.render('HOLD', False, 'white')
        self.queue_rect = self.queue_surface.get_rect(center = ((SIDEBAR_WIDTH+PADDING*2)/2, PADDING*2))

    def get_shape(self, shape):
        self.shape = shape

    def display_queue(self):
        if self.shape:
            hold_block_surface = pygame.image.load(f'Graphics/{self.shape}.png').convert_alpha()
            hold_block_rect = hold_block_surface.get_rect(center = (SIDEBAR_WIDTH/2, 120))
            self.image.blit(hold_block_surface, hold_block_rect)

    def update(self):
        self.display_surface.blit(self.image, self.rect)

        #draw border and fill
        self.image.fill(GRAY)
        pygame.draw.rect(self.display_surface, 'white', self.rect, 2, 2)

        #display text
        self.display_surface.blit(self.queue_surface, self.queue_rect)
        self.display_queue()