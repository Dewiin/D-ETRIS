from settings import *

class Timer():
    def __init__(self, cooldown, repeated=False, func = None):
        #general
        self.cooldown = cooldown
        self.repeated = repeated
        self.func = func
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
        if current_time - self.start_time >= self.cooldown and self.activated:
            if self.func and self.start_time != 0:
                self.func()
            #reset timer
            self.deactivate()
            #repeat timer
            if self.repeated:
                self.activate()
        
