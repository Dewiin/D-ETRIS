from settings import *

class Timer():
    def __init__(self, repeated):
        self.start_time = 0
        self.activated = False

    def activate(self):
        self.activated = True
        self.start_time = pygame.time.get_ticks()
    
    def deactivate(self):
        self.activated = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.activated:
            if current_time - self.start_time >= 800:
                return True
            
        
