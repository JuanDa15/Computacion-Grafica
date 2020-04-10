import pygame
import random
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
drawPlane(window,middle)
end = False
ScreenPosition = []
CartesianPositions = []
RotatedPositions = []
RotatedPositionsScreen = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ScreenPosition.append(event.pos)
                    CartesianCoords = ScreenToCart(middle,event.pos)
                    CartesianPositions.append(CartesianCoords)
                if event.button == 3:
                    if len(ScreenPosition) == 3:
                        CreateTriangleList(window,ScreenPosition,[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
                if event.button == 4:
                    for pos in CartesianPositions:
                        RotatedPositions.append(escalar(pos,1.1))
                    CartesianPositions = RotatedPositions
                    for pos in CartesianPositions:
                        RotatedPositionsScreen.append(CartToScreen(middle,pos))
                    if len(RotatedPositionsScreen) == 3:
                        window.fill([0,0,0])
                        drawPlane(window,middle)
                        CreateTriangleList(window,RotatedPositionsScreen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
                        RotatedPositionsScreen = []
                        RotatedPositions = []
                if event.button == 5:
                    for pos in CartesianPositions:
                        RotatedPositions.append(escalar(pos,0.9))
                    CartesianPositions = RotatedPositions
                    for pos in CartesianPositions:
                        RotatedPositionsScreen.append(CartToScreen(middle,pos))
                    if len(RotatedPositionsScreen) == 3:
                        window.fill([0,0,0])
                        drawPlane(window,middle)
                        CreateTriangleList(window,RotatedPositionsScreen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
                        RotatedPositionsScreen = []
                        RotatedPositions = []