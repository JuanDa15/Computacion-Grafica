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
a2 = PolarToCartesian(100,30)
a3 = Traslacion(a2,0,100)
a4 = PolarToCartesian(50,210)
a5 = Traslacion(a4,0,-50)
a6 = PolarToCartesian(50,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)

PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s]


##SEGUNDA CARA
b1 = PolarToCartesian(50,150)
b2 = Traslacion(b1,0,50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)


SegundaCara = [a1s,b1s,b2s,a6s]


#TERCER POLIGONO
c1 = PolarToCartesian(50,210)
c2 = Traslacion(c1,0,50)

c1s = CartToScreen(b1s,c1)
c2s = CartToScreen(b1s,c2)

TercerCara = [b1s,c1s,c2s,b2s]

#CUARTO POLIGONO
d1 = PolarToCartesian(50,150)
d2 = Traslacion(d1,0,50)

d1s = CartToScreen(c1s,d1)
d2s = CartToScreen(c1s,d2)

CuartaCara = [c1s,d1s,d2s,c2s]

#quinta cara
e1 = PolarToCartesian(50,30)
e2 = PolarToCartesian(50,150)
e3 = PolarToCartesian(50,30)

e1s = CartToScreen(d2s,e1)
e2s = CartToScreen(e1s,e2)
e3s = CartToScreen(e2s,e3)


QuintaCara = [a5s,a6s,b2s,c2s,d2s,e1s,e2s,e3s]

#sexta cara
f1 = PolarToCartesian(50,150)
f2 = PolarToCartesian(50,30)

f1s = CartToScreen(a4s,f1)
f2s = CartToScreen(f1s,f2)


SextaCara = [a3s,a4s,f1s,f2s]

#septima cara
g1 = Traslacion(f1,0,50)
g2 = PolarToCartesian(50,30)

g1s = CartToScreen(a4s,g1)
g2s = CartToScreen(g1s,g2)

SeptimaCara = [f1s,g1s,g2s,f2s]

#octava cara

h1 = PolarToCartesian(100,150)
h2 = PolarToCartesian(50,30)

h1s = CartToScreen(g1s,h1)
h2s = CartToScreen(h1s,h2)

OctavaCara = [g1s,h1s,h2s,g2s]


#NOVENA CARA

NovenaCara = [a5s,e3s,h1s,g1s,f1s,a4s]

#decima cara

DecimaCara = [e1s,e2s,d2s]
if __name__ == "__main__":
    #drawPlane(window,middle)
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
        drawPolygon(window,SelectColor('Red'),OctavaCara)
        drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
