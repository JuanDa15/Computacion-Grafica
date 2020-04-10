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
a2 = PolarToCartesian(125,30)
a3 = Traslacion(a2,0,150)
a4 = PolarToCartesian(50,210)
a5 = Traslacion(a4,0,-100)
a6 = PolarToCartesian(75,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)

PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s]

##SEGUNDA CARA
b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)


SegundaCara = [a1s,b1s,b2s,a6s]


#TERCER POLIGONO
c1 = PolarToCartesian(75,30)

c1s = CartToScreen(b2s,c1)

TercerCara = [b2s,c1s,a5s,a6s]

#CUARTO POLIGONO
d1 = Traslacion(c1,0,75)
d2 = PolarToCartesian(50,330)
d3 = Traslacion(d2,0,-25)
d4 = PolarToCartesian(50,330)
d5 = Traslacion(d4,0,50)

d1s = CartToScreen(b2s,d1)
d2s = CartToScreen(d1s,d2)
d3s = CartToScreen(d1s,d3)
d4s = CartToScreen(d3s,d4)
d5s = CartToScreen(d3s,d5)

CuartaCara = [a5s,c1s,d1s,d2s,d3s,d4s,d5s,a4s]

#quinta cara
e1 = PolarToCartesian(50,30)

e1s = CartToScreen(d5s,e1)

QuintaCara = [a3s,a4s,d5s,e1s]

#sexta cara
SextaCara = [d3s,d4s,d5s]

#septima cara
f1 =PolarToCartesian(50,30)

f1s = CartToScreen(d2s,f1)

SeptimaCara = [d2s,d3s,d5s,f1s]

#octava cara

g1 = PolarToCartesian(50,30)

g1s = CartToScreen(d1s,g1)


OctavaCara = [g1s,f1s,d2s,d1s]

"""
#NOVENA CARA
i1 = PolarToCartesian(175,30)

i1s = CartToScreen(h2s,i1)


NovenaCara = [h2s,i1s,f1s,g2s]


#decima cara
g1 = PolarToCartesian(75,30)

g1s = CartToScreen(i1s,g1)

DecimaCara = [f2s,i1s,g1s,f3s]

#onceaba cara
j1 = PolarToCartesian(50,150)

j1s = CartToScreen(g1s,j1)

OnceavaCara = [i1s,i2s,j1s,g1s]
"""
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
        """drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
        drawPolygon(window,SelectColor('Red'),OnceavaCara)"""