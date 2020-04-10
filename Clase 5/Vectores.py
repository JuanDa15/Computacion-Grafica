import pygame
from LibreriaGeneral import *

pygame.init()

Red = 255
Green = 0
Blue = 0
Color = [15,240,0]
width = 1366
high = 768
window = pygame.display.set_mode([width,high])
middle = updateMiddle([width/2,high/2])
drawPlane(window,middle)
flag = 0
end = False 
ColorSwap = True
positions = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    ColorSwap = True
                    if len(positions) == 2:
                        positions = []
                    CreatePoint(window,ConvertIntList(event.pos),[Red,Green,Blue])
                    createLine(window,middle,event.pos,[Red,Green,Blue])
                    positions.append(ScreenToCart(middle,event.pos))
                if event.button == 1:
                    if len(positions) == 2:
                        producto = vectorAdd(positions[0],positions[1])
                        if ColorSwap == True:
                            if Red <= 15:
                                Red = 255
                                Green = 0
                            Red = Red - 30
                            Green = Green + 30
                            flag += 1
                        if flag < 9:
                            pygame.draw.line(window, [Red + 30,Green - 30,Blue], middle, [middle[0] + producto[0], middle[1] - producto[1]] , 1)
                            pygame.display.flip()
                            ColorSwap = False
                        else:
                            pygame.draw.line(window,Color, middle, [middle[0] + producto[0], middle[1] - producto[1]] , 1)
                            pygame.display.flip()
                            ColorSwap = False
                            flag = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window.fill([0,0,0])
                    drawPlane(window,middle)