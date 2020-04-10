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
a2 = PolarToCartesian(175,150)
a3 = Traslacion(a2,0,50)
a4 = PolarToCartesian(150,330)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)


PrimerCara = [a1s,a2s,a3s,a4s]

##SEGUNDA CARA
b1 = PolarToCartesian(75,30)
b2 = PolarToCartesian(150,330)

b1s = CartToScreen(a3s,b1)
b2s = CartToScreen(b1s,b2)


SegundaCara = [a4s,a3s,b1s,b2s]


#TERCER POLIGONO
c1 = Traslacion(b1,0,75)
c2 = PolarToCartesian(100,330)

c1s = CartToScreen(a3s,c1)
c2s = CartToScreen(c1s,c2)

TercerCara = [b1s,c1s,c2s,b2s]

#CUARTO POLIGONO
d1 = PolarToCartesian(50,30)
d2 = PolarToCartesian(100,330)

d1s = CartToScreen(c1s,d1)
d2s = CartToScreen(d1s,d2)

CuartaCara = [c1s,d1s,d2s,c2s]

#quinta cara
e1 = PolarToCartesian(125,30)

e1s = CartToScreen(a1s,e1)

QuintaCara = [a1s,a4s,b2s,c2s,d2s,e1s]
"""
#sexta cara
f1 = PolarToCartesian(100,30)
f2 = PolarToCartesian(50,330)
f3 = PolarToCartesian(75,30)
f4 = PolarToCartesian(25,330)
f5 = PolarToCartesian(50,210)
f6 = Traslacion(f5,0,-25)

f1s = CartToScreen(e2s,f1)
f2s = CartToScreen(f1s,f2)
f3s = CartToScreen(f2s,f3)
f4s = CartToScreen(f3s,f4)
f5s = CartToScreen(f4s,f5)
f6s = CartToScreen(f4s,f6)

SextaCara = [a5s,a6s,b2s,c1s,c2s,d2s,e2s,f1s,f2s,f3s,f4s,f5s,f6s]

#septima cara
SeptimaCara = [a4s,a5s,f6s,f5s]


#octava cara

h1 = PolarToCartesian(75,30)


h1s = CartToScreen(f5s,h1)


OctavaCara = [a3s,a4s,f5s,h1s]

#NOVENA CARA
i1 = Traslacion(f2,0,50)
i2 = PolarToCartesian(50,150)

i1s = CartToScreen(f1s,i1)
i2s = CartToScreen(i1s,i2)

NovenaCara = [f2s,i1s,i2s,f1s]


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