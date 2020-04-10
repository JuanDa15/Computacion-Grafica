import pygame
from LibreriaGeneral import *

pygame.init()

width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]

end = False
positionsScreen = []
CartesianPos = []
RotatedPos = []
RotatedPosScreen =[]
FirstPos = []
BlockKey = True
angle = 0
if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if BlockKey:
                        FirstPos = ConvertIntList(event.pos)
                        BlockKey = False
                    positionsScreen.append(ConvertIntList(event.pos))
                    CartesianPos.append(ScreenToCart(middle,ConvertIntList(event.pos)))
                if event.button == 4:
                    for pos in CartesianPos:
                        RotatedPoint = RotacionHoraria(pos,angle)
                        RotatedPos.append(RotatedPoint)
                        RotatedPosScreen.append(CartToScreen(middle,RotatedPoint))
                    if len(RotatedPosScreen) == 3:
                        window.fill([0,0,0])
                        CreateTriangle(window,FirstPos,RotatedPosScreen[1],RotatedPosScreen[2])
                        RotatedPos = []
                        RotatedPosScreen = []
                        angle +=1
                if event.button == 5:
                    for pos in CartesianPos:
                        RotatedPoint = RotacionHoraria(pos,angle)
                        RotatedPos.append(RotatedPoint)
                        RotatedPosScreen.append(CartToScreen(middle,RotatedPoint))
                    if len(RotatedPosScreen) == 3:
                        window.fill([0,0,0])
                        CreateTriangle(window,FirstPos,RotatedPosScreen[1],RotatedPosScreen[2])
                        RotatedPos = []
                        RotatedPosScreen = []
                        angle -=1                   
                    
                    