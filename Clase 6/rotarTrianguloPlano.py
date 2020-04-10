#impottacion de librerias
import pygame
import random
import math
from LibreriaGeneral import *
pygame.init()
#-----------------------------------------------
#Definicion de la pantalla
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
#------------------------------------------------
#Definicion de variables
middle = [width/2,high/2]
drawPlane(window,middle)
end = False
ScreenPosition = []
CartesianPositions = []
RotatedPositions = []
RotatedPositionsScreen = []
angulo = 0
#-----------------------------------------------
if __name__ == "__main__":
    while not end:
        drawPlane(window,middle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ScreenPosition.append(event.pos)
                    CartesianPositions.append(ScreenToCart(middle,event.pos))
                    if len(ScreenPosition) == 3:
                        CreateTriangleList(window,ScreenPosition,[255,255,255])
                if event.button == 4:
                    for pos in CartesianPositions:
                        PosRotada = RotacionHoraria(pos,angulo)
                        RotatedPositionsScreen.append(CartToScreen(middle,PosRotada))
                    if len(RotatedPositionsScreen) == 3:
                        CreateTriangleList(window,RotatedPositionsScreen,[255,255,255])
                        RotatedPositionsScreen = []
                        angulo += 3
                if event.button == 5:
                    for pos in CartesianPositions:
                        PosRotada = RotacionHoraria(pos,angulo)
                        RotatedPositionsScreen.append(CartToScreen(middle,PosRotada))
                    if len(RotatedPositionsScreen) == 3:
                        CreateTriangleList(window,RotatedPositionsScreen,[255,255,255])
                        RotatedPositionsScreen = []
                        angulo -= 3