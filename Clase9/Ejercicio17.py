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
a2 = PolarToCartesian(175,30)
a3 = Traslacion(a2,0,150)
a4 = PolarToCartesian(50,210)
a5 = Traslacion(a4,0,-50)
a6 = PolarToCartesian(75,210)
a7 = Traslacion(a6,0,50)
a8 = PolarToCartesian(50,210)


a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)
a7s = CartToScreen(a5s,a7)
a8s = CartToScreen(a7s,a8)



PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s,a7s,a8s]


##SEGUNDA CARA
b1 = PolarToCartesian(125,150)
b2 = Traslacion(b1,0,150)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)


SegundaCara = [a1s,b1s,b2s,a8s]

#TERCER POLIGONO
c1 = PolarToCartesian(50,30)


c1s = CartToScreen(b2s,c1)


TercerCara = [b2s,c1s,a7s,a8s]


#CUARTO POLIGONO

aux1 = PolarToCartesian(75,150)
aux2 = Traslacion(aux1,0,150)
aux3 = PolarToCartesian(50,30)

aux1s = CartToScreen(a1s,aux1)
aux2s = CartToScreen(a1s,aux2)
aux3s = CartToScreen(aux2s,aux3)

d1 = PolarToCartesian(50,330)
d2 = PolarToCartesian(25,30)

d1s = CartToScreen(aux2s,aux3)
d2s = CartToScreen(d1s,d2)

CuartaCara = [d1s,d2s,a5s,a6s,a7s]


#quinta cara
e1 = Traslacion(d2,0,50)


e1s = CartToScreen(d1s,e1)

QuintaCara = [a4s,a5s,d2s,e1s]

#sexta cara
f1 = PolarToCartesian(50,30)


f1s = CartToScreen(e1s,f1)

SextaCara = [e1s,f1s,a3s,a4s]

"""
#septima cara
g1 = PolarToCartesian(50,210)
g2 = Traslacion(g1,0,100)

g1s = CartToScreen(d1s,g1)
g2s = CartToScreen(d1s,g2)

SeptimaCara = [d1s,g1s,g2s,d2s]


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