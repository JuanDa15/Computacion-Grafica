import pygame
from LibreriaGeneral import *

pygame.get_init()

width = 1080
high = 720
 
window = pygame.display.set_mode([width,high])
end = False
LeftList = []
RightList = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
            #    end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                IntPosi = [int (event.pos[0]),int (event.pos[1])]
                PullPoints(window,IntPosi,event.button,LeftList,RightList)
        UpdatePoint(window,LeftList,RightList)