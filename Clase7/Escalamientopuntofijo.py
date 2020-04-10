import pygame
from LibreriaGeneral import *

pygame.init()

width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,600]
drawPlane(window,middle)
end = False

positions = []
positionsCart = []
positionsTranslated = []
positionsTranslatedScreen = []
positionsScalatedScreen = []
posScreenTras = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    positions.append(ConvertIntList(event.pos))
                    positionsCart.append(ScreenToCart(middle,event.pos))
                    if len(positions) == 3:
                        CreateTriangleList(window,positions,[255,255,255])
                if event.button == 3:
                    puntoBeta = [positionsCart[0][0] * -1, positionsCart[0][1] * -1]
                    for pos in positionsCart:
                        PosTrasladada = Traslacion(pos,puntoBeta[0],puntoBeta[1])
                        positionsTranslated.append(PosTrasladada)
                        positionsTranslatedScreen.append(CartToScreen(middle,PosTrasladada))
                    if len(positionsTranslatedScreen) == 3:
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                if event.button == 2:
                    for pos in positionsTranslated:
                        PosEscalada = escalar(pos,2)
                        positionsScalatedScreen.append(CartToScreen(middle,PosEscalada))
                    if len(positionsScalatedScreen) == 3:
                        CreateTriangleList(window,positionsScalatedScreen,[255,255,255])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    for pos in positionsTranslated:
                        PosTrasladada = Traslacion(pos,positionsCart[0][0],positionsCart[0][1])
                        posScreenTras.append((CartToScreen(middle,PosTrasladada)))
                    if len(posScreenTras) == 3:
                        CreateTriangleList(window,posScreenTras,[255,0,0])