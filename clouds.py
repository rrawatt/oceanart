import pygame
import random
from pygame.locals import *

pygame.init()

class Cloud:

    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def draw_obj(self):
        pygame.draw.rect(self.surface, (189,208,231), (self.x, self.y, 70, 20))
        pygame.draw.rect(self.surface, (189,208,231), (self.x+10, self.y-10, 50, 40))
    
    def update_loc(self, x, y):
        self.x = x
        self.y = y
