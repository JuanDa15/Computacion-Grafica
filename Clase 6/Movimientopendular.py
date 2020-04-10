import pygame
from LibreriaGeneral import *

pygame.init()

reloj = pygame.time.Clock()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,0/2]
drawPlane(window,middle)
WHITE = [255,255,255]
angulo = 0
verification = True
end = False

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        puntoInicial = [540,319]
        PuntoCartesiano = ScreenToCart(middle,puntoInicial)
        PuntoRotadoCart = RotacionHoraria(PuntoCartesiano,angulo)
        PuntoRotadoPantalla = CartToScreen(middle,PuntoRotadoCart)
        window.fill([0,0,0])
        drawPlane(window,middle)
        CreatePoint(window,PuntoRotadoPantalla,WHITE)
        createLine(window,middle,PuntoRotadoPantalla,WHITE)
        if verification:
            angulo+=1
            if angulo>60:
                verification = False
        else:
            angulo-=1
            if angulo < -60:
                verification = True
                
        reloj.tick(30)