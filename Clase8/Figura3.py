import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
radius = 100
angle = 0
end = False
Positionspolygon = []
FinalLinePosition = []

if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        Createcircle(window,middle,[0,0,0],radius)
        Createcircle(window,middle,SelectColor('Green'),radius/2)
        SecondRadius = 3*(radius/2)
        Createcircle(window,middle,SelectColor('Light Blue'),SecondRadius)
        AngleMovement = 360/4
        CartesianPos = PolarToCartesian(radius,angle)
        ScreenPos = CartToScreen(middle,CartesianPos)
        Positionspolygon.append(ScreenPos)
        if len(Positionspolygon) == 4:
            drawPolygon(window,[5,5,0],Positionspolygon)
        for position in range(len(Positionspolygon)):
            Createcircle(window,Positionspolygon[position],SelectColor('Red'),radius/2)
        angle += AngleMovement
        
        
        