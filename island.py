import pygame
from pygame.locals import *
import math

pygame.init()

class Island:

    def __init__(self,surface):
        self.surface=surface
    
    def island(self):
        island_points=[]
        for angle in range(0, 360, 1):
            radian = math.radians(angle)
            
            amplitude_variation = 100 * math.sin(0.125*angle)
            
            displacement = amplitude_variation * math.sin(math.radians(angle))
            
            x = 500 + (2000 + displacement) * math.cos(radian)
            y = 2500 + (2000 + displacement) * math.sin(radian)
            island_points.append((x, y))
        return island_points

    def draw(self, angle):
        island_points=self.island()

        rotated_points = []

        for point in island_points:

            x_rel = point[0] - 500
            y_rel = point[1] - 2500

            new_x = x_rel * math.cos(math.radians(angle)) - y_rel * math.sin(math.radians(angle))
            new_y = x_rel * math.sin(math.radians(angle)) + y_rel * math.cos(math.radians(angle))

            rotated_points.append((new_x + 500, new_y + 2500))
            

        pygame.draw.polygon(self.surface, (44, 174, 102), rotated_points)