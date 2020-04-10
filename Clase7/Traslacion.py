import pygame
from LibreriaGeneral import *

pygame.init()

width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
drawPlane(window,middle)
end = False

positions = []
positionsCart = []
positionsTranslatedScreen = []

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
                    for pos in positionsCart:
                        PosTrasladada = Traslacion(pos,-50,0)
                        positionsTranslatedScreen.append(CartToScreen(middle,PosTrasladada))
                    if len(positionsTranslatedScreen) == 3:
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                    
                        