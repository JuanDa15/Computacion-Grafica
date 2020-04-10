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
a3 = Traslacion(a2,0,50)
a4 = PolarToCartesian(175,210)


a1s = CartToScreen(middle,a1)
a2s = CartToScreen(a1s,a2)
a3s = CartToScreen(a1s,a3)
a4s = CartToScreen(a3s,a4)



PrimerCara = [a1s,a2s,a3s,a4s]

##SEGUNDA CARA
b1 = PolarToCartesian(125,150)
b2 = Traslacion(b1,0,50)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)


SegundaCara = [a1s,b1s,b2s,a4s]

#TERCER POLIGONO
c1 = PolarToCartesian(75,30)
c2 = PolarToCartesian(125,330)

c1s = CartToScreen(b2s,c1)
c2s = CartToScreen(c1s,c2)

TercerCara = [a4s,b2s,c1s,c2s]

#CUARTO POLIGONO
d1 = Traslacion(c1,0,75)
d2 = PolarToCartesian(50,330)

d1s = CartToScreen(b2s,d1)
d2s = CartToScreen(d1s,d2)

CuartaCara = [c1s,d1s,d2s,c2s]

#quinta cara
e1 = PolarToCartesian(100,30)
e2 = PolarToCartesian(50,330)

e1s = CartToScreen(d1s,e1)
e2s = CartToScreen(e1s,e2)

QuintaCara = [d1s,e1s,e2s,d2s]

#sexta cara
SextaCara = [c2s,d2s,e2s,a3s]

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