import pygame
from LibreriaGeneral import *
white = [255,255,255]

pygame.init()

width = 1080
high = 720
window = pygame.display.set_mode([width,high])
middle = [width/2,high/2]
drawPlane(window,middle)
end = False

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                carte = ScreenToCart(middle,ConvertIntList(event.pos))
                CreatePoint(window,event.pos,white)
                print carte