import pygame
from pygame.locals import *
import math

pygame.init()

class Beach:

    def __init__(self,surface):
        self.surface=surface

    def draw(self,n):
        
        wave_points = []
        for x in range(-500, 501, 1):
            ang=math.atan(x/1700)
            y = (-((1800+n)*math.cos(ang)-1650)+800)
            wave_points.append(((x+500), y))

        pygame.draw.circle(self.surface, (0,157,196), (500,2500), 2000)
        pygame.draw.polygon(self.surface, (229,216,144), wave_points + [(1000, 800), (0, 800)])