import pygame
import random
import math
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
angulo = 1
if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    PuntoCartesiano = CartToScreen(middle,event.pos)
                    CreatePoint(window,event.pos,[255,255,255])
                    createLine(window,middle,event.pos,[255,255,255])
                if event.button == 4:
                    CartesianCoords = ScreenToCart(middle,punto)
                    RotacionCartesiana = RotacionHoraria(CartesianCoords,angulo)
                    RotacionPantalla = CartToScreen(middle,RotacionCartesiana)
                    pygame.draw.circle(window, [255,255,255], RotacionPantalla, 2)
                    createLine(window,middle,RotacionPantalla,[255,255,255])
                    drawPlane(window,middle)
                    pygame.display.flip()
                    CartesianCoords = RotacionPantalla
                    angulo +=1
                if event.button == 5:
                    CartesianCoords = ScreenToCart(middle,punto)
                    RotacionCartesiana = RotacionHoraria(CartesianCoords,angulo)
                    RotacionPantalla = CartToScreen(middle,RotacionCartesiana)
                    pygame.draw.circle(window, [255,255,255], RotacionPantalla, 2)
                    createLine(window,middle,RotacionPantalla,[255,255,255])
                    drawPlane(window,middle)
                    pygame.display.flip()
                    CartesianCoords = RotacionPantalla
                    angulo -=1