import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1280
high =920
window = pygame.display.set_mode([width,high])
middle = [width/2,high]
end = False

#Primer Poligono
A1 = [0,0]
A2 = PolarToCartesian(500,40)
A3 = Traslacion(A2,0,200)
Aaux1 = PolarToCartesian(300,40)
A4 = Traslacion(Aaux1,0,200)
A5 = Traslacion(A4,0,200)
Aaux2 = PolarToCartesian(200,40)
A6 = Traslacion(Aaux2,0,200)
A7 = Traslacion(A6,0,200)
A8 = Traslacion(A1,0,200)

A1s = CartToScreen(middle,A1)
A2s = CartToScreen(middle, A2)
A3s = CartToScreen(middle,A3)
A4s = CartToScreen(middle,A4)
A5s = CartToScreen(middle,A5)
A7s = CartToScreen(middle,A7)
A6s = CartToScreen(middle,A6)
A8s = CartToScreen(middle,A8)


#TERCER POLIGONO
B1 = PolarToCartesian(300,150)


B1s = CartToScreen(middle,B1)
B2s = CartToScreen(A8s,B1)
#CUARTO POLIGONO
C1 = PolarToCartesian(300,150)

C1s = CartToScreen(A6s,C1)

#QUINTO POLIGONO
D1 = PolarToCartesian(300,150)

D1s = CartToScreen(A7s,D1)

#Sexto Poligono
E1 = PolarToCartesian(300,150)

E1s = CartToScreen(A5s,E1)

#Segundo Poligono
PrimerCara = [A1s,A2s,A3s,A4s,A5s,A7s,A6s,A8s]
SegundaCara = [A3s,A4s,A5s]
TercerCara = [A1s,B1s,B2s,A8s]
CuartaCara = [A6s,A8s,B2s,C1s]
QuintaCara = [A7s,A6s,C1s,D1s]
SextaCara = [A5s,A7s,D1s,E1s]

if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        drawPolygon(window,SelectColor('Red'),PrimerCara)
        drawPolygon(window,SelectColor('Red'),SegundaCara)
        drawPolygon(window,SelectColor('Red'),TercerCara)
        drawPolygon(window,SelectColor('Red'),CuartaCara)
        drawPolygon(window,SelectColor('Red'),QuintaCara)
        drawPolygon(window,SelectColor('Red'),SextaCara)