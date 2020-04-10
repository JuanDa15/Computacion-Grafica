import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
drawPlane(window,middle)
middle = [width/2,high/2]
TrianglePos = []
TriangleCar = []
TriangleRotatedCar = []
TriangleRotated = []
key = True
end  = False
angulo = 0

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if key:
                        StaticPoint = event.pos
                        key = False
                    TrianglePos.append(ConvertIntList(event.pos))
                    if len(TrianglePos) == 3:
                        CreateTriangle(window,StaticPoint,TrianglePos[1],TrianglePos[2])
                if event.button == 4:
                    for pos in TrianglePos:
                        TriangleCar.append(ScreenToCart(middle,ConvertIntList(pos)))
                    for pos in TriangleCar:
                        TriangleRotatedCar.append(RotacionHoraria(pos,angulo))
                    for pos in TriangleRotatedCar:
                        TriangleRotated.append(CartToScreen(middle,pos))
                    if len(TriangleRotated) == 3:
                        window.fill([0,0,0])
                        drawPlane(window,middle)
                        CreateTriangle(window,StaticPoint,TriangleRotated[1],TriangleRotated[2])
                        angulo += 1
                        TriangleRotatedCar = []
                        TriangleCar = []
                        TriangleRotated = []
                if event.button == 5:
                    for pos in TrianglePos:
                        TriangleCar.append(ScreenToCart(middle,ConvertIntList(pos)))
                    for pos in TriangleCar:
                        TriangleRotatedCar.append(RotacionHoraria(pos,angulo))
                    for pos in TriangleRotatedCar:
                        TriangleRotated.append(CartToScreen(middle,pos))
                    if len(TriangleRotated) == 3:
                        window.fill([0,0,0])
                        drawPlane(window,middle)
                        CreateTriangle(window,StaticPoint,TriangleRotated[1],TriangleRotated[2])
                        angulo -= 1
                        TriangleRotatedCar = []
                        TriangleCar = []
                        TriangleRotated = []
                        