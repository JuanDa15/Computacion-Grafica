import pygame
from LibreriaGeneral import *

pygame.init()
WHITE = [255,255,255]
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = width/2,high/2
drawPlane(window,middle)
end = False 
positionsScreen = []
positionsCart = []
Escaladaspositions = []
if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    positionsScreen.append(ConvertIntList(event.pos))
                if event.button == 3:
                    if len(positionsScreen) == 3:
                        for pos in positionsCart:
                            positions.append(CartToScreen(middle,pos))
                        for pos in positionsScreen:
                            Escaladaspositions.append(escalar(pos,2))
                        CreateTriangleList(window,positionsScreen)
                        CreateTriangleList(window,Escaladaspositions)