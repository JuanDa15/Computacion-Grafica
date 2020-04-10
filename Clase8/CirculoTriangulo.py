import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
angle = 0
end = False
PositionsTriangle = []

if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        Createcircle(window,middle,SelectColor('Light Blue'),200)
        AngleMovement = 360/3
        CartesianPos = PolarToCartesian(200,angle)
        ScreenPos = CartToScreen(middle,CartesianPos)
        PositionsTriangle.append(ScreenPos)
        angle += AngleMovement
        if len(PositionsTriangle) == 3:
            CreateTriangleList(window,PositionsTriangle,SelectColor('Red'))
        