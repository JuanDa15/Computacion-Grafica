import pygame
from LibreriaGeneral import *
white = [255,255,255]
Xcoord = 0
pygame.init()

pend = 0
corte = 0
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
drawPlane(window,middle)
end = False
positions = []
positionsScreen = []
if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    carte = ScreenToCart(middle,ConvertIntList(event.pos))
                    positions.append(carte)
                    positionsScreen.append(event.pos)
                    if len(positions) == 2:
                        pend = getSlope(positions[0],positions[1])
                        corte = corteY(positions[0],pend)
                        createLine(window,positionsScreen[0],positionsScreen[1],white)
                elif event.button == 3:
                    recta(window,middle,pend,corte)
                    positions = []
                    positionsScreen = []
