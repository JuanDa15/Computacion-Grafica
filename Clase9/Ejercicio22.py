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
a3 = Traslacion(a2,0,100)
aux1 = PolarToCartesian(100,30)
a4 = Traslacion(aux1,0,125)
aux2 = PolarToCartesian(50,30)
a5 = Traslacion(aux2,0,125)
a6 = Traslacion(a1,0,100)


a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a1s,a4)
a5s = CartToScreen(a1s,a5)
a6s = CartToScreen(a1s,a6)

PrimerCara = [a1s,a2s,a3s,a4s,a5s,a6s]

##SEGUNDA CARA
b1 = PolarToCartesian(125,150)
b2 = Traslacion(b1,0,125)
b3 = PolarToCartesian(50,330)
b4 = Traslacion(b3,0,-25)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(b2s,b3)
b4s = CartToScreen(b2s,b4)

SegundaCara = [a1s,b1s,b2s,b3s,b4s,a6s]

#TERCER POLIGONO
c1 = PolarToCartesian(150,30)
c2 = PolarToCartesian(50,330)
c3 = PolarToCartesian(50,210)
c4 = PolarToCartesian(50,210)


c1s = CartToScreen(b2s,c1)
c2s = CartToScreen(c1s,c2)
c3s = CartToScreen(c2s,c3)
c4s = CartToScreen(c3s,c4)

TercerCara = [b3s,b2s,c1s,c2s,c3s,a4s,a5s,c4s]

#CUARTO POLIGONO
CuartaCara = [b4s,b3s,c4s]

#quinta cara
e1 = Traslacion(c2,0,-25)

e1s = CartToScreen(c1s,e1)

QuintaCara = [c2s,c3s,e1s]

#sexta cara
SextaCara = [a3s,a4s,c3s,e1s]

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