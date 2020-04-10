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
a2 = PolarToCartesian(200,30)
a3 = Traslacion(a2,0,175)
a4 = PolarToCartesian(50,210)
a5 = Traslacion(a4,0,-100)
a6 = PolarToCartesian(150,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)


PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s]

##SEGUNDA CARA
b1 = PolarToCartesian(125,150)
b2 = Traslacion(b1,0,175)
b3 = PolarToCartesian(50,330)
b4 = Traslacion(b3,0,-100)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(b2s,b3)
b4s = CartToScreen(b2s,b4)


SegundaCara = [a1s,b1s,b2s,b3s,b4s,a6s]

#TERCER POLIGONO
c1 = PolarToCartesian(75,30)

c1s = CartToScreen(b4s,c1)

TercerCara = [a5s,a6s,b4s,c1s]

#CUARTO POLIGONO
d1 = Traslacion(c1,0,100)

d1s = CartToScreen(b4s,d1)

CuartaCara = [b3s,b4s,c1s,d1s]

#quinta cara
QuintaCara = [a4s,a5s,c1s,d1s]

#sexta cara
f1 = PolarToCartesian(200,30)

f1s = CartToScreen(b2s,f1)

SextaCara = [b2s,f1s,a3s,a4s,d1s,b3s]

"""
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
        drawPolygon(window,SelectColor('Red'),SextaCara)
        """drawPolygon(window,SelectColor('Red'),SeptimaCara)
        drawPolygon(window,SelectColor('Red'),OctavaCara)
        drawPolygon(window,SelectColor('Red'),NovenaCara)
        drawPolygon(window,SelectColor('Red'),DecimaCara)
        drawPolygon(window,SelectColor('Red'),OnceavaCara)"""