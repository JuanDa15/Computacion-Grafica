import pygame
import random
import math
from LibreriaGeneral import *
pygame.init()
#-------------------------------------------------------------
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
end = False
ScreenPosition = []
RotatedPositionsScreen = []
angulo = 0
#-------------------------------------------------------------
if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ScreenPosition.append(event.pos)
                    if len(ScreenPosition) == 3:
                        CreateTriangleList(window,ScreenPosition,[255,255,255])
                if event.button == 4:
                    for pos in ScreenPosition:
                        RotatedPositionsScreen.append(RotacionHoraria(pos,angulo))
                    if len(RotatedPositionsScreen) == 3:
                        CreateTriangleList(window,RotatedPositionsScreen,[255,255,255])
                        RotatedPositionsScreen = []
                        angulo +=1
                if event.button == 5:
                    for pos in ScreenPosition:
                        RotatedPositionsScreen.append(RotacionHoraria(pos,angulo))
                    if len(RotatedPositionsScreen) == 3:
                        CreateTriangleList(window,RotatedPositionsScreen,[255,255,255])
                        RotatedPositionsScreen = []
                        angulo -=1