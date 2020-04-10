import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window =pygame.display.set_mode([width,high])
positions = []
end = False

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    point1 = [100,200]
                    point2 = [350,200]
                    point3 = [200,350]
                    CreateTriangle(window,point1,point2,point3)
                elif event.button == 3:
                    positions.append(ConvertIntList(event.pos))
                    if len(positions) == 3:
                        CreateTriangleList(window,positions)
                        positions = []