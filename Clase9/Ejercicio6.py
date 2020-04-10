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
a2 = PolarToCartesian(150,150)
a3 = Traslacion(a2,0,75)
a4 = PolarToCartesian(75,330)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(middle,a2)
a3s = CartToScreen(middle,a3)
a4s = CartToScreen(a3s,a4)

PrimerCara = [a1s,a2s,a3s,a4s]

#SEGUNDA CARA
b1 = PolarToCartesian(75,30)
b2 = PolarToCartesian(75,30)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a4s,b2)

SegundaCara = [a4s,a1s,b1s,b2s]

#TERCER POLIGONO
c1 = PolarToCartesian(75,30)


c1s = CartToScreen(a3s,c1)

TercerCara = [a3s,a4s,b2s,c1s]

#CUARTO POLIGONO

d1 = Traslacion(b1,0,150)
d2 = PolarToCartesian(150,150)

d1s = CartToScreen(middle,d1)
d2s = CartToScreen(d1s,d2)


CuartaCara = [c1s,b2s,b1s,d1s,d2s]

#quinta cara

e1 = PolarToCartesian(75,30)
e2 = Traslacion(e1,0,150)

e1s = CartToScreen(b1s,e1)
e2s = CartToScreen(b1s,e2)

QuintaCara = [b1s,e1s,e2s,d1s]

#sexta cara
f1 = PolarToCartesian(150,150)

f1s = CartToScreen(e2s,f1)


SextaCara = [e2s,d1s,d2s,f1s]

#septima cara
#g1 = PolarToCartesian(50,150)

#g1s = CartToScreen(d3s,g1)

#SeptimaCara = [d3s,d2s,f1s,g1s]

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
        #drawPolygon(window,SelectColor('Red'),SeptimaCara)