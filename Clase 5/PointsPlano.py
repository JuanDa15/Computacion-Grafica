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
                    CreatePoint(window,event.pos,[255,255,255])
                    transformada = transformada1Cuadrante(middle,event.pos)
                    CreatePoint(window,transformada,[255,255,255])
                    screen = CartToScreen(middle,transformada)
                    print screen