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
a2 = PolarToCartesian(75,30)
a3 = Traslacion(a2,0,50)
a4 = PolarToCartesian(75,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)

PrimerCara = [a1s,a2s,a3s,a4s]


##SEGUNDA CARA
b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,50)
b3 = PolarToCartesian(50,330)
b4 = Traslacion(b3,0,50)
b5 = PolarToCartesian(25,150)
b6 = Traslacion(b5,0,50)
b7 = PolarToCartesian(100,330)
b8 = Traslacion(b7,0,-50)
b9 = PolarToCartesian(25,150)
b10 = Traslacion(b9,0,-50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(b2s,b3)
b4s = CartToScreen(b2s,b4)
b5s = CartToScreen(b4s,b5)
b6s = CartToScreen(b4s,b6)
b7s = CartToScreen(b6s,b7)
b8s = CartToScreen(b6s,b8)
b9s = CartToScreen(b8s,b9)
b10s = CartToScreen(b8s,b10)

SegundaCara = [a1s,b1s,b2s,b3s,b4s,b5s,b6s,b7s,b8s,b9s,b10s,a4s]

#TERCER POLIGONO
TercerCara = [b2s,b3s,b4s]


#CUARTO POLIGONO
d1 = PolarToCartesian(75,30)
d2 = PolarToCartesian(100,330)

d1s = CartToScreen(b6s,d1)
d2s = CartToScreen(d1s,d2)

CuartaCara = [b6s,d1s,d2s,b7s]


#quinta cara
e1 = Traslacion(d2,0,-50)

e1s = CartToScreen(d1s,e1)

QuintaCara = [b8s,b7s,d2s,e1s]


#sexta cara
f1 = PolarToCartesian(25,210)
f2 = Traslacion(f1,0,-25)


f1s = CartToScreen(e1s,f1)
f2s = CartToScreen(e1s,f2)

SextaCara = [f1s,b8s,b9s,b10s,f2s]

#septima cara
SeptimaCara = [b10s,a4s,a3s,f2s]

"""
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
        drawPolygon(window,SelectColor('Red'),SeptimaCara)
        """drawPolygon(window,SelectColor('Red'),OctavaCara)
        drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
        drawPolygon(window,SelectColor('Red'),OnceavaCara)"""