import pygame
import math
from pygame.locals import *

pygame.init()

class Sunmoon:

    def __init__(self,n,surface,x,y):
        self.n=n
        self.x=x
        self.y=y
        self.surface=surface
    
    def pixel(self,x,y):
        if self.n==0:
            pygame.draw.rect(self.surface, (255,224,106), (x, y, 20, 20))
        else:
            pygame.draw.rect(self.surface, (207,212,209), (x, y, 20, 20))

    def draw_obj(self):
        if self.n==0:
            for i in range(0,360,10):
                for j in range(0,66,13):
                    tempx=self.x+15*((j*math.cos(3.14/180*i))//15)
                    tempy=self.y+15*((j*math.sin(3.14/180*i))//15)
                    self.pixel(tempx,tempy) 
        else:
            for i in range(0,360,10):
                for j in range(0,41,10):
                    tempx=self.x+15*((j*math.cos(3.14/180*i))//15)
                    tempy=self.y+15*((j*math.sin(3.14/180*i))//15)
                    self.pixel(tempx,tempy) 

    def update_center(self, x, y):
        self.x = x
        self.y = y
    
