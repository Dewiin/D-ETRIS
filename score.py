from settings import *

class Score():
    def __init__(self):
        #general
        self.image = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*SCORE_HEIGHT_FRACTION))
        self.rect = self.image.get_rect(topleft = (PADDING*2 + GAME_WIDTH, PADDING + GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION))
        self.display = pygame.display.get_surface()

        #font
        self.game_font = pygame.font.Font('Graphics/Russo_One.ttf', 30)
        self.score, self.level, self.lines_cleared = 0, 1, 0

    def scoring_info(self, score, level, lines_cleared):
        self.score = score
        self.level = level
        self.lines_cleared = lines_cleared

    def display_score(self):
        #display score and info
        for i, text in enumerate([f'Score: {self.score}', f'Level: {self.level}', f'Lines: {self.lines_cleared}']):
            score_surfaces = self.game_font.render(text, False, 'white')
            score_rects = score_surfaces.get_rect(center = (self.image.get_width()/2, i * self.image.get_height()/3 + 30))
            self.image.blit(score_surfaces, score_rects)

    def update(self):
        self.display.blit(self.image, self.rect)

        #draw border and fill
        self.image.fill(GRAY)
        pygame.draw.rect(self.display, 'white', self.rect, 2, 2)    

        #display score
        self.display_score()    