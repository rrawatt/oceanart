import pygame
from pygame.locals import *
import random
import sunmoon
import stars
import math
import clouds
import beach
import island

pygame.init()

golden_sand = (242, 209, 107)
sky_blue = (135, 206, 235)
black = (0, 0, 0)
sun_yellow=(255,224,106)
moon_silver=(207,212,209)
star_blue=(184,222,230)

dusk_night_dawn=[(232,129,127),(195,114,124),(141,82,115),(90,51,110),(90,51,110),(49,31,98),(30,43,88),(37,53,105),
                 (37,53,105),(53,50,131),(72,69,154),(97,76,191),(97,76,191),(72,69,154),(53,50,131),(37,53,105),
                 (37,53,105),(30,43,88),(49,31,98),(90,51,110),(90,51,110),(141,82,115),(195,114,124),(232,129,127)]
dawn_day_dusk=[(232,129,127),(229,149,114),
    (177, 137, 127), (176, 161, 161), (177, 169, 169), (136, 170, 170), (128, 164, 169), 
     (105, 151, 165), (104, 156, 175), (104, 156, 175), (73, 154, 172), (53, 133, 156), 
     (53, 133, 156), (73, 154, 172), (104, 156, 175), (104, 156, 175), (105, 151, 165), 
     (128, 164, 169), (136, 170, 170), (177, 169, 169), (176, 161, 161), (177, 137, 127)
     ,(232,129,127),(229,149,114)
]
cycle=dawn_day_dusk+dusk_night_dawn

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ocean Grid")



def main():
    run = True
    clock = pygame.time.Clock()
    fps = 60

    ang=180

    sun=sunmoon.Sunmoon(0,WIN,0,0)
    moon=sunmoon.Sunmoon(1,WIN,0,0)
    cloud=[]
    for i in range(4):
        cloud.append(clouds.Cloud(WIN,random.randint(0,1000),random.randint(0,300)))

    beachside=beach.Beach(WIN)
    beachsidesand=0
    beachsidesandstate=0
    
    star=[]
    num = [0, 1, 2]
    weights = [0.3, 0.4, 0.3]
    for i in range(25):
        
        x=stars.Stars(random.choices(num,weights)[0], WIN, 0,0)
        r1=range(30,500)
        r2=range(-500,-30)
        rad=random.choice(list(r1)+list(r2))
        angl=random.uniform(0,360) 
        star.append([x,rad,angl])
    
    updateval=int(fps/7.5)

    time=0
    while run:

        if time!=47*updateval:
            WIN.fill(cycle[time//updateval])
            time+=1
        else:
            WIN.fill(cycle[time//updateval])
            time=0

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        n=random.randint(1,50)

        for i in star:
            coss = math.cos(math.pi / 360 * i[2])
            sins = math.sin(math.pi / 360 * i[2])
            i[0].update_center(500 + i[1] * coss, 400 + i[1] * sins)
            i[0].draw_obj()
            i[2] += 5/updateval
    
        cossm=math.cos(3.14/180*ang)
        sinsm=math.sin(3.14/180*ang)
        sun.update_center(500+400*cossm,400+300*sinsm)
        sun.draw_obj()
        moon.update_center(500-250*cossm,400-200*sinsm)
        moon.draw_obj()

        ang+=(7.5/updateval)

        for i in range(len(cloud)):
            cloud[i].draw_obj()
            if cloud[i].x>=1000:
                cloud[i].update_loc(random.randint(-100,-70), random.randint(0,300))
            cloud[i].update_loc(cloud[i].x + random.randint(5,15)/updateval, cloud[i].y)
        
        island_=island.Island(WIN)
        island_.draw(-ang/10)
        
        beachside.draw(beachsidesand)

        if beachsidesandstate==0:
            beachsidesand+=2.5/updateval
        else:
            beachsidesand-=2.5/updateval
        if beachsidesand > 25:
            beachsidesandstate=1
        elif beachsidesand<-25:
            beachsidesandstate=0

        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

if __name__ == '__main__':
    main()
