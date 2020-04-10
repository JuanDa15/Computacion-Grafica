import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high]
end = False

#Primer Poligono
A1 = [0,0]
A2 = PolarToCartesian(300,20)
Aaux1 = PolarToCartesian(200,20)
A3 = Traslacion(A2,0,250)
A4 = PolarToCartesian(100,200)
A5 = Traslacion(Aaux1,0,100)
A6 = PolarToCartesian(200,200)

A1s = CartToScreen(middle,A1)
A2s = CartToScreen(middle,A2)
A3s = CartToScreen(middle,A3)
A4s = CartToScreen(A3s,A4)
A5s = CartToScreen(middle,A5)
A6s = CartToScreen(A5s,A6)
#---------------------------------------------------
#Segundo Poligono
B1 = PolarToCartesian(350,150)
B2 = Traslacion(B1,0,100)
B3 = PolarToCartesian(350,-30)

B1s = CartToScreen(middle,B1)
B2s = CartToScreen(middle,B2)
B3s = CartToScreen(B2s,B3)

#----------------------------------------------------
#Tercer Poligono
C1 = PolarToCartesian(200,20)

C1s = CartToScreen(B2s,C1)
#---------------------------------------------------
#cuarto poligono
D1 = PolarToCartesian(350,150)

D1s = CartToScreen(A4s,D1)
#---------------------------------------------------
#quinta cara
E1 = PolarToCartesian(100,20)

E1s = CartToScreen(D1s,E1)

PrimerCara = [A1s,A2s,A3s,A4s,A5s,A6s]
SegundaCara = [A1s,B1s,B2s,B3s]
TercerCara = [A5s,A6s,B2s,C1s]
CuartaCara = [A4s,A5s,C1s,D1s]
QuintaCara = [A3s,A4s,D1s,E1s]

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