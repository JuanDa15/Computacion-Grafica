import pygame
from LibreriaGeneral import *
pygame.init()
#----------------------------------------------------
width = 1280
high =920
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
end = False

#PRIMERA CARA

a1 = [0,0]
a2 = PolarToCartesian(150,30)
a3 = Traslacion(a2,0,50)
a4 = PolarToCartesian(150,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(middle,a2)
a3s = CartToScreen(middle,a3)
a4s = CartToScreen(a3s,a4)

PrimerCara = [a1s,a2s,a3s,a4s]

#SEGUNDA CARA
#a1 -a1s
#a4 -a4s

b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,150)
b3 = PolarToCartesian(50,330)
baux1 = PolarToCartesian(100,150)
b4 = Traslacion(baux1,0,50)

b1s = CartToScreen(middle,b1)
b2s = CartToScreen(middle,b2)
b3s = CartToScreen(b2s,b3)
b4s = CartToScreen(middle,b4)

SegundaCara = [a1s,b1s,b2s,b3s,b4s,a4s]

#TERCER POLIGONO
c1 = PolarToCartesian(150,30)

c1s = CartToScreen(b4s,c1)

TercerCara = [a3s,a4s,b4s,c1s]

#CUARTO POLIGONO

d1 = PolarToCartesian(100,30)
d2 = Traslacion(d1,0,50)
d3 = PolarToCartesian(50,30)

d1s = CartToScreen(b3s,d1)
d2s = CartToScreen(b3s,d2)
d3s = CartToScreen(d2s,d3)
CuartaCara = [c1s,b4s,b3s,d1s,d2s,d3s]
#quinta cara
e1 = PolarToCartesian(100,30)

e1s = CartToScreen(b2s,e1)

QuintaCara = [b2s,e1s,d1s,b3s]
#sexta cara
f1 = Traslacion(e1,0,50)

f1s = CartToScreen(b2s,f1)


SextaCara = [d1s,e1s,f1s,d2s]

#septima cara
g1 = PolarToCartesian(50,150)

g1s = CartToScreen(d3s,g1)

SeptimaCara = [d3s,d2s,f1s,g1s]

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
        drawPolygon(window,SelectColor('Red'),SeptimaCara)