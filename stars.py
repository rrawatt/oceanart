import pygame
from pygame.locals import *

pygame.init()

class Stars:
    def __init__(self,n,surface,x,y):
        self.n=n
        self.x=x
        self.y=y
        self.surface=surface

    def draw_obj(self):
        if self.n==0:
            pygame.draw.rect(self.surface, (202,244,253), (self.x, self.y, 10, 10))
        elif self.n==1:
            pygame.draw.rect(self.surface, (202,244,253), (self.x, self.y,5, 5))
        elif self.n==2:
            pygame.draw.rect(self.surface, (202,244,253), (self.x, self.y, 5, 5))
            pygame.draw.rect(self.surface, (170, 226, 253), (self.x+5,self.y, 5, 5))
            pygame.draw.rect(self.surface, (170, 226, 253), (self.x,self.y-5, 5, 5))
            pygame.draw.rect(self.surface, (170, 226, 253), (self.x-5,self.y, 5, 5))
            pygame.draw.rect(self.surface, (170, 226, 253), (self.x,self.y+5, 5, 5))
        
    
    def update_center(self, x, y):
        self.x = x
        self.y = y

        
