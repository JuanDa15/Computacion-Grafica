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
        Createcircle(window,middle,SelectColor('Light Blue'),radius)
        SecondRadius = 2*radius
        Createcircle(window,middle,SelectColor('Light Blue'),SecondRadius)
        AngleMovement = 360/4
        CartesianPos2 = PolarToCartesian(SecondRadius,(angle + 45))
        CartesianPos = PolarToCartesian(radius,angle)
        ScreenPos2 = CartToScreen(middle,CartesianPos2)
        ScreenPos = CartToScreen(middle,CartesianPos)
        Positionspolygon.append(ScreenPos)
        FinalLinePosition.append(ScreenPos2)
        if len(Positionspolygon) == 4:
            drawPolygon(window,SelectColor('Yellow'),Positionspolygon)
        for position in range(len(Positionspolygon)):
            createLine(window,Positionspolygon[position],FinalLinePosition[position],SelectColor('Green'))
        angle += AngleMovement
        
        
        