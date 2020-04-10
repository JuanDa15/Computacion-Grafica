import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1080
high =720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
end = False

#Primer Poligono
A1 = [0,0]
A2 = PolarToCartesian(150,20)
A3 = Traslacion(A2,0,100)
Aaux1 = PolarToCartesian(100,20)
A4 = Traslacion(Aaux1,0,100)
A5 = Traslacion(Aaux1,0,50)
A6 = PolarToCartesian(100,200)

A1s = CartToScreen(middle,A1)
A2s = CartToScreen(middle,A2)
A3s = CartToScreen(middle,A3)
Aaux1s = CartToScreen(middle,Aaux1)
A4s = CartToScreen(middle,A4)
A5s = CartToScreen(middle,A5)
A6s = CartToScreen(A5s,A6)

#Segundo Poligono
B1 = PolarToCartesian(150,160)
Baux1 = PolarToCartesian(100,160)
B2 = Traslacion(B1,0,150)
B3 = Traslacion(Baux1,0,150)
B4 = Traslacion(Baux1,0,50)

B1s = CartToScreen(middle,B1)
B2s = CartToScreen(middle,B2)
B3s = CartToScreen(middle,B3)
B4s = CartToScreen(middle,B4)

#TercerPoligono
C1 = PolarToCartesian(100,20)

C1s = CartToScreen(B4s,C1)

#Cuarto Poligono
D1 = PolarToCartesian(100,160)

D1s = CartToScreen(A4s,D1)

#Quinto Poligono
E1 = PolarToCartesian(50,20)

E1s = CartToScreen(D1s,E1)

#Sexto Poligono
F1 = PolarToCartesian(150,20)

F1s = CartToScreen(B3s,F1)

#Septimo Poligono

G1 = PolarToCartesian(150,20)

G1s = CartToScreen(B2s,G1)
#------------------------------------------------------

FirstFace = [A1s,A2s,A3s,A4s,A5s,A6s]
SecondFace = [A1s,B1s,B2s,B3s,B4s,A6s]
ThirdFace = [A6s,B4s,C1s,A5s]
FourthFace = [A5s,C1s,D1s,A4s]
FithFace = [A3s,A4s,D1s,E1s]
SixFace = [B4s,B3s,F1s,E1s,D1s,C1s]
SevenFace = [B2s,B3s,F1s,G1s]

if __name__ == "__main__":
    drawPlane(window,middle)
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        drawPolygon(window,SelectColor('Green'),FirstFace)
        drawPolygon(window,SelectColor('Green'),SecondFace)
        drawPolygon(window,SelectColor('Green'),ThirdFace)
        drawPolygon(window,SelectColor('Green'),FourthFace)
        drawPolygon(window,SelectColor('Green'),FithFace)
        drawPolygon(window,SelectColor('Green'),SixFace)
        drawPolygon(window,SelectColor('Green'),SevenFace)
        
        
        