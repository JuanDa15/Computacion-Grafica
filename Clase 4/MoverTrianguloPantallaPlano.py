import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
positions = [[100,200],[350,200],[200,350]]
positionsPlane = []
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
                    positionsPlane = []
                elif event.button == 1:
                    for pos in positions:
                        transformada = transformada4Cuadrante(middle,pos)
                        positionsPlane.append(transformada)
                        if len(positions) == 3:
                            CreateTriangleList(window,positions)
                        if len(positionsPlane) == 3:
                            CreateTriangleList(window,positionsPlane)
            if event.type == pygame.KEYDOWN:
                window.fill([0,0,0])
                drawPlane(window,middle)
                if event.key == pygame.K_LEFT:
                    for pos in positions:
                        pos[0] = pos[0] - 2
                        if pos[0] < 0:
                            pos[0] = 1080
                        CreateTriangleList(window,positions)
                    for pos in positionsPlane:
                        pos[0] = pos[0] - 2
                        if pos[0] < 0:
                            pos[0] = 1080
                        CreateTriangleList(window,positionsPlane)
                if event.key == pygame.K_RIGHT:
                    for pos in positions:
                        pos[0] = pos[0] + 2
                        if pos[0] > 1080:
                            pos[0] = 0
                        CreateTriangleList(window,positions)
                    for pos in positionsPlane:
                        pos[0] = pos[0] + 2
                        if pos[0] > 1080:
                            pos[0] = 0
                        CreateTriangleList(window,positionsPlane)