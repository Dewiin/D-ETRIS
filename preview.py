from settings import *

class Preview():
    def __init__(self):
        self.image = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION - PADDING))
        self.rect = self.image.get_rect(topleft = (PADDING*2 + GAME_WIDTH, PADDING))
        self.display = pygame.display.get_surface()

    def update(self):
        self.display.blit(self.image, self.rect)