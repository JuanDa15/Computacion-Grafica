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
a2 = PolarToCartesian(125,150)
a3 = Traslacion(a2,0,125)
a4 = PolarToCartesian(50,330)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)


PrimerCara = [a1s,a2s,a3s,a4s]

##SEGUNDA CARA
b1 = PolarToCartesian(125,30)
b2 = PolarToCartesian(50,150)

b1s = CartToScreen(a4s,b1)
b2s = CartToScreen(b1s,b2)

SegundaCara = [a3s,b2s,b1s,a4s]

#TERCER POLIGONO
c1 = PolarToCartesian(125,30)
c2 = PolarToCartesian(75,30)
c3 = Traslacion(c2,0,50)
c4 = PolarToCartesian(50,30)


c1s = CartToScreen(a1s,c1)
c2s = CartToScreen(a1s,c2)
c3s = CartToScreen(a1s,c3)
c4s = CartToScreen(c3s,c4)

TercerCara = [c1s,c2s,c3s,c4s]

#CUARTO POLIGONO
d1 = PolarToCartesian(25,150)
d2 = PolarToCartesian(50,210)

d1s = CartToScreen(c4s,d1)
d2s = CartToScreen(d1s,d2)

CuartaCara = [c3s,c4s,d1s,d2s]

#quinta cara
QuintaCara = [c2s,c3s,d2s]

#sexta cara
SextaCara = [c2s,a1s,a4s,b1s,d1s,d2s]

"""
#septima cara
SeptimaCara = [b10s,a4s,a3s,f2s]


#octava cara

h1 = PolarToCartesian(75,150)
h2 = Traslacion(h1,0,100)

h1s = CartToScreen(g1s,h1)
h2s = CartToScreen(g1s,h2)


OctavaCara = [g1s,h1s,h2s,g2s]

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
        """drawPolygon(window,SelectColor('Red'),SeptimaCara)
        drawPolygon(window,SelectColor('Red'),OctavaCara)
        drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
        drawPolygon(window,SelectColor('Red'),OnceavaCara)"""