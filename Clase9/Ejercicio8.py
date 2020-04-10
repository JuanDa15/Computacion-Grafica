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
a3 = Traslacion(a2,0,50)
a4 = PolarToCartesian(100,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(middle,a2)
a3s = CartToScreen(middle,a3)
a4s = CartToScreen(a3s,a4)


PrimerCara = [a1s,a2s,a3s,a4s]

#SEGUNDA CARA
b1 = PolarToCartesian(50,150)
b2 = Traslacion(b1,0,50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)


SegundaCara = [a1s,b1s,b2s,a4s]

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
e1 = PolarToCartesian(150,30)
e2 = PolarToCartesian(100,30)
e3 = PolarToCartesian(50,330)
e4 = PolarToCartesian(50,30)

e1s = CartToScreen(d2s,e1)
e2s = CartToScreen(d2s,e2)
e3s = CartToScreen(e2s,e3)
e4s = CartToScreen(e3s,e4)

QuintaCara = [a3s,a4s,b2s,c2s,d2s,e2s,e3s,e4s]

#sexta cara
f1 = PolarToCartesian(50,330)
f2 = Traslacion(f1,0,50)
f3 = PolarToCartesian(50,210)
f4 = Traslacion(f3,0,-50)

f1s = CartToScreen(e1s,f1)
f2s = CartToScreen(e1s,f2)
f3s = CartToScreen(f2s,f3)
f4s = CartToScreen(f2s,f4)

SextaCara = [f1s,f2s,f3s,f4s]

#septima cara
g1 = PolarToCartesian(50,150)
g2 = Traslacion(g1,0,50)

g1s = CartToScreen(f4s,g1)
g2s = CartToScreen(f4s,g2)

SeptimaCara = [f4s,g1s,g2s,f3s]

#octava cara

h1 = PolarToCartesian(50,30)

h1s = CartToScreen(g2s,h1)

OctavaCara = [f2s,f3s,g2s,h1s]

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
        #drawPolygon(window,SelectColor('Red'),SeptimaCara)
