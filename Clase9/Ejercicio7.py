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
a3 = Traslacion(a2,0,150)
a4 = PolarToCartesian(50,210)
a5 = Traslacion(a4,0,-100)
a6 = PolarToCartesian(100,210)

a1s = CartToScreen(middle,a1)
a2s = CartToScreen(middle,a2)
a3s = CartToScreen(middle,a3)
a4s = CartToScreen(a3s,a4)
a5s = CartToScreen(a3s,a5)
a6s = CartToScreen(a5s,a6)


PrimerCara = [a1s,a2s,a3s,a4s,a4s,a5s,a6s]

#SEGUNDA CARA
b1 = PolarToCartesian(150,150)
b2 = Traslacion(b1,0,150)
b3 = PolarToCartesian(50,330)

b1s = CartToScreen(a1s,b1)
b2s = CartToScreen(a1s,b2)
b3s = CartToScreen(b2s,b3)

SegundaCara = [a1s,b1s,b2s,b3s,a6s]

#TERCER POLIGONO
c1 = PolarToCartesian(100,30)


c1s = CartToScreen(b3s,c1)

TercerCara = [a6s,b3s,c1s,a5s]

#CUARTO POLIGONO

CuartaCara = [a5s,c1s,a4s]

#quinta cara

e1 = PolarToCartesian(150,30)

e1s = CartToScreen(b2s,e1)

QuintaCara = [c1s,b3s,b2s,e1s,a3s,a4s]

#sexta cara
#f1 = PolarToCartesian(150,150)

#f1s = CartToScreen(e2s,f1)


#SextaCara = [e2s,d1s,d2s,f1s]

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
        
