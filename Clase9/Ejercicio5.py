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

a1 = PolarToCartesian(75,30)
a2 = PolarToCartesian(150,30)
a3 = Traslacion(a2,0,125)
a4 = PolarToCartesian(75,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(middle,a2)
a3s = CartToScreen(middle,a3)
a4s = CartToScreen(a3s,a4)

PrimerCara = [a1s,a2s,a3s,a4s]

#SEGUNDA CARA
#a1 -a1s
#a4 -a4s

b1 = PolarToCartesian(75,150)

b1s = CartToScreen(a4s,b1)

SegundaCara = [a1s,a4s,b1s]

#TERCER POLIGONO
c1 = PolarToCartesian(75,210)
c2 = [0,0]

c1s = CartToScreen(b1s,c1)
c2s = CartToScreen(middle,c2)

TercerCara = [b1s,c1s,c2s,a1s]

#CUARTO POLIGONO

d1 = PolarToCartesian(150,150)
d2 = Traslacion(d1,0,125)

d1s = CartToScreen(middle,d1)
d2s = CartToScreen(middle,d2)


CuartaCara = [c1s,c2s,d1s,d2s]

#quinta cara

e1 = PolarToCartesian(150,30)

e1s = CartToScreen(d2s,e1)

QuintaCara = [a3s,a4s,b1s,c1s,d2s,e1s]
#sexta cara
#f1 = Traslacion(e1,0,50)

#f1s = CartToScreen(b2s,f1)


#SextaCara = [d1s,e1s,f1s,d2s]

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
        #drawPolygon(window,SelectColor('Red'),SextaCara)
        #drawPolygon(window,SelectColor('Red'),SeptimaCara)