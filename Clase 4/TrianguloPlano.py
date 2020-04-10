import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
positions = [[100,200],[350,200],[200,350]]
positionsPlane = []
positionsDisplay = []
middle = []
end = False

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    middle = updateMiddle(ConvertIntList(event.pos))
                    drawPlane(window,middle)
                elif event.button == 1:
                    for pos in positions:
                        transformada = transformada4Cuadrante(middle,pos)
                        positionsPlane.append(transformada)
                        if len(positions) == 3:
                            CreateTriangleList(window,positions)
                        if len(positionsPlane) == 3:
                            CreateTriangleList(window,positionsPlane)
                            for poss in positionsPlane:
                                screen = transformToScreen(middle,poss)
                                positionsDisplay.append(screen)
                                print positionsDisplay
                            positionsDisplay = []
                            positionsPlane = []
                        