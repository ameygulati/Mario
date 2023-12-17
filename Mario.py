class Enemy:
    def __init__(self,koopa,spiny,goomba):
        self.koopa=koopa
        self.spiny=spiny
        self.goomba=goomba
    
class Item:
    def __init__(self,coin,mushroom,shell):
        self.coin=coin
        self.mushroom=mushroom
        self.shell=shell


import pygame
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Mario")
clock=pygame.time.Clock

t1=pygame.image.load("freetileset/png/Tiles/2.png")
t1 = pygame.transform.scale(t1, (50,50))

m = pygame.image.load("flatboy/png/Idle(1).png")
m = pygame.transform.scale(m,(50,50))

bg_start=pygame.image.load("freegui/png/BG.png")
bg_start=pygame.transform.scale(bg_start,(600,600))

def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size,bold=True,italic=True)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

l=[[0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,2,1,0,0,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,1,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,1,1,1,1],
   [0,0,0,1,1,1,0,0,0,0,0,0],
   [0,0,1,1,1,1,1,0,0,0,0,0],
   [1,1,1,1,1,1,1,1,1,1,1,1]]

while True:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()