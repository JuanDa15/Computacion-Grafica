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
a3 = Traslacion(a2,0,25)
a4 = PolarToCartesian(125,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)

PrimerCara = [a1s,a2s,a3s,a4s]

##SEGUNDA CARA
aux1 = PolarToCartesian(125,150)
aux2 = PolarToCartesian(75,150)
aux3 = PolarToCartesian(25,150)

b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,25)
b3 = Traslacion(aux1,0,50)
b4 = Traslacion(aux1,0,100)
b5 = Traslacion(aux2,0,150)
b6 = Traslacion(aux3,0,100)
b7 = Traslacion(aux3,0,50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(a1s,b3)
b4s = CartToScreen(a1s,b4)
b5s = CartToScreen(a1s,b5)
b6s = CartToScreen(a1s,b6)
b7s = CartToScreen(a1s,b7)

SegundaCara = [a1s,b1s,b2s,b3s,b4s,b5s,b6s,b7s,a4s]

#TERCER POLIGONO
c1 = PolarToCartesian(125,30)

c1s = CartToScreen(b7s,c1)

TercerCara = [a4s,b7s,c1s,a3s]

#CUARTO POLIGONO
d1 = PolarToCartesian(125,30)

d1s = CartToScreen(b6s,d1)

CuartaCara = [b6s,d1s,c1s,b7s]

#quinta cara
e1 = PolarToCartesian(125,30)

e1s = CartToScreen(b5s,e1)

QuintaCara = [b5s,b6s,d1s,e1s]

"""
#sexta cara
f1 = PolarToCartesian(25,210)
f2 = Traslacion(f1,0,-25)


f1s = CartToScreen(e1s,f1)
f2s = CartToScreen(e1s,f2)

SextaCara = [f1s,b8s,b9s,b10s,f2s]

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
        """drawPolygon(window,SelectColor('Red'),SextaCara)
        drawPolygon(window,SelectColor('Red'),SeptimaCara)
        drawPolygon(window,SelectColor('Red'),OctavaCara)
        drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
        drawPolygon(window,SelectColor('Red'),OnceavaCara)"""