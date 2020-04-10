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
positionsTranslated = []
positionsTranslatedScreen = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    positions.append(ConvertIntList(event.pos))
                    if len(positions) == 3:
                        CreateTriangleList(window,positions,[255,255,255])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for pos in positions:
                        positionsCart.append(ScreenToCart(middle,pos))
                    for pos in positionsCart:
                        positionsTranslated.append(Traslacion(pos,-3,0))
                    for pos in positionsTranslated:
                        positionsTranslatedScreen.append(CartToScreen(middle,pos))
                    if len(positionsTranslatedScreen) == 3:
                        drawPlane(window,middle)
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                        positions = positionsTranslatedScreen
                        positionsCart = []
                        positionsTranslated = []
                        positionsTranslatedScreen = []
                        window.fill([0,0,0])
                if event.key == pygame.K_RIGHT:
                    for pos in positions:
                        positionsCart.append(ScreenToCart(middle,pos))
                    for pos in positionsCart:
                        positionsTranslated.append(Traslacion(pos,3,0))
                    for pos in positionsTranslated:
                        positionsTranslatedScreen.append(CartToScreen(middle,pos))
                    if len(positionsTranslatedScreen) == 3:
                        drawPlane(window,middle)
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                        positions = positionsTranslatedScreen
                        positionsCart = []
                        positionsTranslated = []
                        positionsTranslatedScreen = []
                        window.fill([0,0,0])
                if event.key == pygame.K_DOWN:
                    for pos in positions:
                        positionsCart.append(ScreenToCart(middle,pos))
                    for pos in positionsCart:
                        positionsTranslated.append(Traslacion(pos,0,-3))
                    for pos in positionsTranslated:
                        positionsTranslatedScreen.append(CartToScreen(middle,pos))
                    if len(positionsTranslatedScreen) == 3:
                        drawPlane(window,middle)
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                        positions = positionsTranslatedScreen
                        positionsCart = []
                        positionsTranslated = []
                        positionsTranslatedScreen = []
                        window.fill([0,0,0])
                if event.key == pygame.K_UP:
                    for pos in positions:
                        positionsCart.append(ScreenToCart(middle,pos))
                    for pos in positionsCart:
                        positionsTranslated.append(Traslacion(pos,0,3))
                    for pos in positionsTranslated:
                        positionsTranslatedScreen.append(CartToScreen(middle,pos))
                    if len(positionsTranslatedScreen) == 3:
                        drawPlane(window,middle)
                        CreateTriangleList(window,positionsTranslatedScreen,[255,255,255])
                        positions = positionsTranslatedScreen
                        positionsCart = []
                        positionsTranslated = []
                        positionsTranslatedScreen = []
                        window.fill([0,0,0])
                